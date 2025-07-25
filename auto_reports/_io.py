from __future__ import annotations

import collections
import io
import itertools
import json
import os
import typing as T
from pathlib import Path

import colorcet as cc
import geopandas as gp
import holoviews as hv
import natsort
import numpy as np
import pandas as pd
import panel as pn
import pyarrow.parquet as pq
import seareport_data as D
import shapely

from auto_reports._storms import STORMS
from auto_reports._storms import THRESHOLDS


def _readline(fd: bytes) -> bytes:
    return fd.readline().split(b"=")[0].split(b"!")[0].strip()


OVERRIDE_CSS = """
:root {
    --hidden: initial !important;
}
* {
    visibility: visible !important;
    overflow: visible !important;
}
"""


def get_data_dir(data_dir: str | Path) -> Path:
    return Path(data_dir)


def get_obs_dir(data_dir: str | Path) -> Path:
    return Path(data_dir) / "obs"


def get_models_dir(data_dir: str | Path) -> Path:
    return Path(data_dir) / "models"


def get_parquet_files(data_dir: str | Path) -> list[Path]:
    model_dir = get_models_dir(data_dir)
    paths = natsort.natsorted(model_dir.glob("*/*.parquet"))
    return paths


def get_model_paths(data_dir: str | Path) -> list[Path]:
    paths = natsort.natsorted(set(path.parent for path in get_parquet_files(data_dir)))
    return paths


def get_model_names(data_dir: str | Path) -> list[str]:
    names = [path.name for path in get_model_paths(data_dir)]
    return names


def get_obs_station_paths(data_dir: str | Path) -> list[Path]:
    obs_dir = get_obs_dir(data_dir)
    paths = natsort.natsorted(obs_dir.glob("*.parquet"))
    return paths


def get_obs_station_names(data_dir: str | Path) -> list[str]:
    names = [path.stem for path in get_obs_station_paths(data_dir)]
    return names


def get_station_names(data_dir: str | Path) -> list[str]:
    stations = set(get_obs_station_names(data_dir))
    for model in get_model_paths():
        stations.update(path.stem for path in model.glob("*.parquet"))
    return natsort.natsorted(stations)


def get_parquet_attrs(path):
    pq_metadata = pq.read_metadata(path)
    return json.loads(pq_metadata.metadata[b"PANDAS_ATTRS"])


def get_observation_metadata(data_dir: str | Path) -> pd.DataFrame:
    df = pd.DataFrame(
        get_parquet_attrs(path) for path in get_obs_station_paths(data_dir)
    )
    return df


@pn.cache
def load_data(path: Path) -> pd.Series:
    df = pd.read_parquet(path)
    if len(df.columns) == 1:
        column = df.columns[0]
    elif "elev" in df.columns:  # for seareport parquet with multiple columns
        column = "elev"
    elif "zeta" in df.columns:
        column = "zeta"
    else:
        raise ValueError(
            f"could not find water level column in parquet file: {df.columns}",
        )
    return df[column]


@pn.cache
def load_world_oceans():
    df = gp.read_file(
        "https://gist.githubusercontent.com/tomsail/2fa52d9667312b586e7d3baee123b57b/raw/f121bd446e7c276e7230fb9896e4d487d63a8cb1/world_maritime_sectors.json",
    )
    return df


@pn.cache
def load_countries(res="c") -> gp.GeoDataFrame:
    path = D.gshhg(res, "5")[0]
    countries = gp.read_file(path)
    polygons = countries[countries.geom_type == "Polygon"]
    return polygons


def find_ocean_for_station(station, oceans_df, xstr="longitude", ystr="latitude"):
    point = shapely.geometry.Point(station[xstr], station[ystr])
    for _, ocean in oceans_df.iterrows():
        if point.within(ocean["geometry"].buffer(0)):
            # Return a tuple with the two desired column values
            return ocean["name"], ocean["ocean"]
    # Return a tuple with None for both values if no match is found
    return None, None


def assign_oceans(df):
    oceans_ = load_world_oceans()
    unique_stations = df.station.unique()
    mapping = {}
    for unique_station in unique_stations:
        s = df[df.station == unique_station].iloc[0]
        mapping[unique_station] = find_ocean_for_station(s, oceans_, "lon", "lat")
    df[["name", "ocean"]] = df.apply(
        lambda station: mapping[station.station],
        axis=1,
        result_type="expand",
    )
    return df


def find_storm(timestamp: pd.Timestamp, storms: dict):
    for name, dates in storms.items():
        for date in dates:
            storm_date = pd.Timestamp(date)
            if abs(timestamp - storm_date) <= pd.Timedelta(hours=48):
                return name
    return None


def assign_storms(ext: pd.DataFrame, region: str):
    ext = ext.sort_values(ascending=False, by="observed").reset_index()
    ext = ext[ext["observed"] > THRESHOLDS[region]]
    ext["storm"] = ext["time observed"].apply(lambda x: find_storm(x, STORMS[region]))
    return ext.dropna(subset="storm")


def update_color_map(df, filter_var):
    # Create a color mapping for oceans or maritime sectors
    unique_oceans = df[filter_var].unique()
    factor = int(len(cc.CET_C6) / len(unique_oceans))
    color_key = hv.Cycle(cc.CET_C6).values
    ocean_mapping = {
        ocean: color_key[i * factor % len(cc.CET_C6)]
        for i, ocean in enumerate(unique_oceans)
    }
    return ocean_mapping


@pn.cache
def parse_hgrid(
    path: os.PathLike[str] | str,
    include_boundaries: bool = False,
    sep: str | None = None,
) -> dict[str, T.Any]:
    """
    Parse an hgrid.gr3 file.

    The function is also able to handle fort.14 files, too, (i.e. ADCIRC)
    but the boundary parsing is not keeping all the available information.
    """
    rvalue: dict[str, T.Any] = {}
    with open(path, "rb") as fd:
        _ = fd.readline()  # skip line
        no_elements, no_points = map(int, fd.readline().strip().split(b"!")[0].split())
        nodes_buffer = io.BytesIO(b"\n".join(itertools.islice(fd, 0, no_points)))
        nodes = np.loadtxt(nodes_buffer, delimiter=sep, usecols=(1, 2, 3))
        elements_buffer = io.BytesIO(b"\n".join(itertools.islice(fd, 0, no_elements)))
        elements = np.loadtxt(
            elements_buffer,
            delimiter=sep,
            usecols=(2, 3, 4),
            dtype=int,
        )
        elements -= 1  # 0-based index for the nodes
        rvalue["nodes"] = nodes
        rvalue["elements"] = elements
        # boundaries
        if include_boundaries:
            boundaries = collections.defaultdict(list)
            no_open_boundaries = int(_readline(fd))
            # total_open_boundary_nodes = int(_readline(fd))
            for i in range(no_open_boundaries):
                no_nodes_in_boundary = int(_readline(fd))
                boundary_nodes = np.genfromtxt(
                    fd,
                    delimiter=sep,
                    usecols=(0,),
                    max_rows=no_nodes_in_boundary,
                    dtype=int,
                )
                boundaries["open"].append(boundary_nodes - 1)  # 0-based index
            # closed boundaries
            no_closed_boundaries = int(_readline(fd))
            # total_closed_boundary_nodes = int(_readline(fd))
            for _ in range(no_closed_boundaries):
                # Sometimes it seems that the closed boundaries don't have a "type indicator"
                # For example: Test_COSINE_SFBay/hgrid.gr3
                # In this cases we assume that boundary type is 0 (i.e. land in schism)
                # XXX Maybe check the source code?
                parsed = _readline(fd).split(b" ")
                if len(parsed) == 1:
                    no_nodes_in_boundary = int(parsed[0])
                    boundary_type = 0
                else:
                    no_nodes_in_boundary, boundary_type = map(int, parsed)
                boundary_nodes = np.genfromtxt(
                    fd,
                    delimiter=sep,
                    usecols=(0,),
                    max_rows=no_nodes_in_boundary,
                    dtype=int,
                )
                boundary_nodes -= 1  # 0-based-index
                boundaries[boundary_type].append(boundary_nodes)
            rvalue["boundaries"] = boundaries
    return rvalue
