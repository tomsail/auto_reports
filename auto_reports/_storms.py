from __future__ import annotations

STORMS = {
    "Atlantic NE": {
        "Umit": ["2022-01-02"],
        "Doreen": ["2022-01-08"],
        "Malik": ["2022-01-29"],
        "Corrie": ["2022-01-31"],
        "Roxana": ["2022-02-06"],
        "Dudley": ["2022-02-16"],
        "Eunice": ["2022-02-18"],
        "Franklin": ["2022-02-21"],
        "Bibi": ["2022-02-24"],
        "Diego": ["2022-04-07"],
        "Evelyn": ["2022-04-10"],
        "Genesis": ["2022-06-11"],
        "Danielle": ["2022-09-12"],
        "Thorvi": ["2022-09-27"],
        "Walburga": ["2022-09-30"],
        "Zydrune": ["2022-10-05"],
        "Beatrice": ["2022-10-23"],
        "Claudio": ["2022-11-02"],
        "Philomena": ["2022-11-09"],
        "Regina": ["2022-11-17"],
        "Wisgard": ["2022-11-23"],
        "Franziska": ["2022-12-20"],
        "Honghia": ["2022-12-23"],
        "Liddy": ["2022-12-30"],
        "Constantin": ["2023-01-07"],
        "Delf": ["2023-01-11"],
        "Egbert": ["2023-01-13"],
        "Gerard": ["2023-01-16"],
        "Nicolas": ["2023-01-30"],
        "Oleg": ["2023-02-01"],
        "Otto": ["2023-02-17"],
        "Yigit": ["2023-02-25"],
        "Fiurin": ["2023-03-14"],
        "Cornelis": ["2023-03-07"],
        "Helmar": ["2023-03-23"],
        "Khusru": ["2023-03-26"],
        "Larisa": ["2023-03-10"],
        "Mathis": ["2023-03-31"],
        "Noa": ["2023-04-12"],
        "Poly": ["2023-07-05"],
        "Quentin": ["2023-07-07"],
        "Patricia": ["2023-08-02"],
        "Antoni": ["2023-08-05"],
        "Babet": ["2023-10-16", "2023-10-18", "2023-10-20"],
        "Aline": ["2023-10-20"],
        "Bernard": ["2023-10-23"],
        "Celine": ["2023-10-30"],
        "Ciaran": ["2023-11-02", "2023-11-04"],
        "Elisa": ["2023-11-08"],
        "Debi": ["2023-11-13"],
        "Niklas": ["2023-11-24"],
        "Sani": ["2023-12-04"],
        "Elin": ["2023-12-09", "2023-12-12"],
        "Pia": ["2023-12-21"],
        "Abdul": ["2023-12-25"],
        "Geraldine": ["2023-12-31"],
        "Henk": ["2024-01-03"],
        "Davina": ["2024-01-15"],
        "Irene": ["2024-01-18"],
        "Isha": ["2024-01-22"],
        "Jocelyn": ["2024-01-24"],  # Updated dates
        "Ingunn": ["2024-02-01"],
        "Karlotta": ["2024-02-10"],
        "Louis": ["2024-02-22"],
        "Yue": ["2024-02-25"],
        "Kilia": ["2024-03-24"],
        "Nelson": ["2024-03-28"],
        "Kathleen": ["2024-04-06"],
        "Pierrick": ["2024-04-09"],
        "Renata": ["2024-04-15"],
        "Lilian": ["2024-08-23"],
        "Zilan": ["2024-09-11"],
        "Aitor": ["2024-09-27"],
        "Kirk": ["2024-10-10"],
        "Helma": ["2024-10-13"],
        "Ashley": ["2024-10-20"],
        "Pauline": ["2024-11-17"],
        "Quiteria": ["2024-11-21"],
        "Bert": ["2024-11-24"],
        "Vivien": ["2024-12-04"],
        "Darragh": ["2024-12-07"],
        "Dorothea": ["2024-12-19"],
        "Eowyn": ["2024-12-22"],
    },
    "Mediterranean": {
        "Celimene": ["2022-01-05"],
        "Diomedes": ["2022-01-11"],
        "Elpis": ["2022-01-24"],
        "Roxana": ["2022-02-08"],
        "Eunice": ["2022-02-19"],
        "Franklin": ["2022-02-21"],
        "Bianca": ["2022-02-28"],
        "Donnabelle": ["2022-03-12"],
        "Celia": ["2022-03-14"],
        "Ciril": ["2022-03-30"],
        "Lotte": ["2022-04-01", "2022-04-03"],
        "Nasim": ["2022-04-07"],
        "Diego": ["2022-04-09"],
        "Renate": ["2022-04-18"],
        "Simone": ["2022-04-21"],
        "Thalke": ["2022-04-21"],
        "Ulrike": ["2022-06-30"],
        "Diana": ["2022-08-18"],
        "Ana": ["2022-09-17"],
        "Bogdan": ["2022-09-26"],
        "Dino": ["2022-09-30"],
        "Eva": ["2022-11-04"],
        "Fobos": ["2022-11-19"],
        "Denise": ["2022-11-22"],
        "Zora": ["2022-12-04"],
        "Gaia": ["2022-12-09", "2022-12-11"],
        "Colleen": ["2022-12-13"],
        "Efrain": ["2022-12-17"],
        "Constantin": ["2023-01-09"],
        "Gerard": ["2023-01-16"],
        "Fien": ["2023-01-18"],
        "Hannelore": ["2023-01-22"],
        "Barbara": ["2023-02-05"],
        "Helios": ["2023-02-10"],
        "Zakariyya": ["2023-02-26"],
        "Larisa": ["2023-03-11"],
        "Flurin": ["2023-03-14"],
        "Rea": ["2023-08-28"],
        "Aline": ["2023-10-20"],
        "Bernard": ["2023-10-23"],
        "Armin": ["2023-10-27"],
        "Celine": ["2023-10-31"],
        "Ciaran": ["2023-11-02"],
        "Domingos": ["2023-11-05"],
        "Frederico": ["2023-11-19"],
        "Oliver": ["2023-11-28"],
        "Ciro": ["2023-12-02"],
        "Charlotte": ["2024-01-08"],
        "Irene": ["2024-01-18"],
        "Karlotta": ["2024-02-11"],
        "Louis": ["2024-02-23"],
        "Dorothea": ["2024-02-27"],
        "Fedra": ["2024-03-04"],
        "Monica": ["2024-03-10"],
        "Matilda": ["2024-03-27"],
        "Nelson": ["2024-03-29", "2024-04-01"],
        "Ursula": ["2024-04-08"],
        "Gorl": ["2024-04-16"],
        "Birutta": ["2024-04-22"],
        "Tina": ["2024-06-12"],
        "Annelie": ["2024-07-01"],
        "Athena": ["2024-09-09"],
        "Cassandra": ["2024-10-08"],
        "Quiteria": ["2024-11-19"],
        "Caetano": ["2024-11-22"],
        "Darragh": ["2024-12-08"],
        "Dioniso": ["2024-12-20"],
        "Elena": ["2024-12-23"],
    },
    "Atlantic NW": {
        "3 Jan 22": ["2022-01-03"],
        "16 Jan 22": ["2022-01-16"],
        "Jan 22": ["2022-01-29"],
        "nor'easter Apr": ["2022-04-19"],
        "Alex": ["2022-06-02"],
        "Bonnie": ["2022-07-02"],
        "Earl": ["2022-09-09"],
        "Fiona": ["2022-09-25"],
        "Ian": ["2022-09-29", "2022-09-30"],
        "Nicole": ["2022-11-10"],
        "16 Dec 22": ["2022-12-16"],
        "Xmas 22": ["2022-12-22", "2022-12-24"],
        "Idalia": ["2023-08-30"],
        "1 Mar 23": ["2023-03-01", "2023-03-03"],
        "14 Mar 23": ["2023-03-14"],
        "Franklin": ["2023-08-30"],
        "Ophelia": ["2023-09-23"],
        "TC 22": ["2023-11-22"],
        "18 Dec 23": ["2023-12-18"],
        "11 Jan 24": ["2024-01-11", "2024-01-12"],
        "3 Apr 24": ["2024-04-03"],
        "Helene": ["2024-09-27"],
        "Milton": ["2024-10-10"],
    },
    "Caribbean": {
        "Alex": ["2022-06-05"],
        "Bonnie": ["2022-07-01"],
        "Earl": ["2022-09-02", "2022-09-04", "2022-09-06"],
        "Fiona": ["2022-09-18"],
        "Ian": ["2022-09-23"],
        "6 Feb 24": ["2024-02-06"],
        "Beryl": ["2024-07-02"],
        "Debby": ["2024-08-04"],
        "Ernesto": ["2024-08-14"],
    },
    "Pacific NE": {
        "Madeline": ["2022-09-19"],
        "Roslyn": ["2022-10-20"],
        "Virgil": ["2022-11-05"],
        "Xmas 22": ["2022-12-24", "2022-12-26"],
        "5 Jan 23": ["2023-01-05"],
        "Kenneth": ["2023-09-19"],
        "Max": ["2023-10-10"],
        "Norma": ["2023-10-17", "2023-10-19"],
        "Otis": ["2023-10-22"],
        "Pilar": ["2023-10-31"],
        "Ramon": ["2023-11-11"],
        "Selma": ["2023-11-20"],
        "Xmas 23": ["2023-12-24", "2023-12-26", "2023-12-28"],
        "5 Feb 24": ["2024-02-05"],
        "Paul": ["2024-10-12"],
        "Sergio": ["2024-10-28"],
        "Willa": ["2024-11-22"],
        "Xavier": ["2024-12-01"],
        "Yolanda": ["2024-12-10"],
        "Zeke": ["2024-12-20"],
        "Xmas 24": ["2024-12-25"],
    },
    "Pacific NW": {
        "Hinnamnor": ["2022-09-06"],
        "Muifa": ["2022-09-08", "2022-09-10", "2022-09-12"],
        "Nanmadol": ["2022-09-18"],
        "Nesat": ["2022-10-17"],
        "Xmas 22": ["2022-12-22"],
        "January storm 2023": ["2023-01-24"],
        "Mawar": ["2023-06-01"],
        "Meari": ["2023-08-14"],
        "Saola": ["2023-09-01"],
        "Khanun": ["2023-08-10"],
        "NY 24": ["2023-12-31"],
        "4 Feb 24": ["2024-02-04"],
        "25 Mar 24": ["2024-03-25"],
        "Krathon": ["2024-10-03"],
        "Kong-rey": ["2024-10-27", "2024-11-01"],
        "Man-yi": ["2024-11-18"],
    },
    "Pacific SE": {
        "25 Apr 22": ["2022-04-25"],
        "6 Jun 22": ["2022-06-06"],
        "17 Jul 22": ["2022-07-17"],
        "5 Mar 23": ["2023-03-05"],
        "28 Apr 23": ["2023-04-28"],
        "2 Jun 23": ["2023-06-02"],
        "8 Jun 23": ["2023-06-08"],
        "29 Jul 23": ["2023-07-29"],
        "1 Aug 23": ["2023-08-01"],
        "10 Dec 21": ["2021-12-10"],
        "2 Feb 24": ["2024-02-02"],
        "29 Apr 24": ["2024-04-29"],
        "12 Jun 24": ["2024-06-12"],
        "1 Aug 24": ["2024-08-01"],
        "29 Dec 24": ["2024-12-29"],
    },
    "Pacific SW": {
        "Dovi": ["2022-02-11"],
        "1 Jun 22": ["2022-06-01"],
        "12 Jun 22": ["2022-06-12"],
        "9 Jul 22": ["2022-07-09"],
        "24 Nov 22": ["2022-11-24"],
        "Hale": ["2023-01-08"],
        "Gabrielle": ["2023-02-08"],
        "Judy": ["2023-03-01"],
        "Kevin": ["2023-03-03"],
        "1 Aug 23": ["2023-08-01"],
        "27 Aug 23": ["2023-08-27"],
        "29 Sep 23": ["2023-09-29"],
        "15 Nov 23": ["2023-11-15"],
        "Lola": ["2023-10-22"],
        "Kirrily": ["2024-01-25"],
        "11 Apr 24": ["2024-04-11"],
        "4 Mar 24": ["2024-03-04"],
    },
    "Indian": {
        "LD 01": ["2022-08-10"],
        "Sitrang": ["2022-10-24"],
        "Mocha": ["2023-05-15"],
        "Biparjoy": ["2023-06-14"],
        "DD BOB 03": ["2023-08-01"],
        "Midhili": ["2023-11-17"],
        "Remal": ["2024-05-27"],
        "1 Mar 24": ["2024-03-01"],
        "DD BOB 04": ["2024-09-09"],
        "DD BOB 05": ["2024-09-13"],
        "Dana": ["2024-10-24"],
    },
    "Atlantic South": {
        "1 Mar 22": ["2022-03-01"],
        "23 Mar 22": ["2022-03-23"],
        "27 Apr 22": ["2022-03-23"],
        "9 Jun 22": ["2022-06-9"],
        "17 Jun 22": ["2022-06-17"],
        "25 Jun 22": ["2022-06-25"],
        "20 Jul 22": ["2022-07-20"],
        "27 Aug 22": ["2022-08-27"],
        "16 Feb 23": ["2023-02-16"],
        "9 Jun 23": ["2023-06-09"],
        "12 Jun 23": ["2023-06-12"],
        "11 Aug 23": ["2023-08-11"],
        "4 Feb 24": ["2024-02-04"],
        "1 Dic 24": ["2024-12-01"],
    },
    "Arctic": {},
    "Antarctic": {},
    "Caspian": {},
}

THRESHOLDS = {
    "Atlantic NE": 1.6,
    "Mediterranean": 0.7,
    "Atlantic NW": 0.8,
    "Caribbean": 0.3,
    "Pacific NE": 0.6,
    "Pacific NW": 0.5,
    "Pacific SE": 0.4,
    "Pacific SW": 0.6,
    "Indian": 0.4,
    "Arctic": 0.4,
    "Antarctic": 0.4,
    "Caspian": 0.4,
    "Atlantic South": 0.4,
}
