ABV_TO_FULL = {
    'crd': 'Arizona Cardinals',
    'atl': 'Atlanta Falcons',
    'rav': 'Baltimore Ravens',
    'buf': 'Buffalo Bills',
    'car': 'Carolina Panthers',
    'chi': 'Chicago Bears',
    'cin': 'Cincinnati Bengals',
    'cle': 'Cleveland Browns',
    'dal': 'Dallas Cowboys',
    'den': 'Denver Broncos',
    'det': 'Detroit Lions',
    'gnb': 'Green Bay Packers',
    'htx': 'Houston Texans',
    'clt': 'Indianapolis Colts',
    'jax': 'Jacksonville Jaguars',
    'kan': 'Kansas City Chiefs',
    'mia': 'Miami Dolphins',
    'min': 'Minnesota Vikings',
    'nwe': 'New England Patriots',
    'nor': 'New Orleans Saints',
    'nyg': 'New York Giants',
    'nyj': 'New York Jets',
    'rai': 'Oakland Raiders',
    'phi': 'Philadelphia Eagles',
    'pit': 'Pittsburgh Steelers',
    'sdg': 'San Diego Chargers',
    'sfo': 'San Francisco 49ers',
    'sea': 'Seattle Seahawks',
    'ram': 'St. Louis Rams',
    'stl': 'St. Louis Rams',
    'tam': 'Tampa Bay Buccaneers',
    'oti': 'Tennessee Titans',
    'was': 'Washington Redskins',
}

FULL_TO_ABV = {full: abv for abv, full in ABV_TO_FULL.items()}


def Abv2Full(team_s):
    result = ABV_TO_FULL.get(team_s)
    if result is None:
        raise ValueError(f"Invalid team abbreviation: '{team_s}'")
    return result


def Full2Abv(team_s):
    result = FULL_TO_ABV.get(team_s)
    if result is None:
        raise ValueError(f"Invalid team name: '{team_s}'")
    return result
