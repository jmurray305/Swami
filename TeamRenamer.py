def Abv2Full(team_s):
    try:
        if team_s == 'crd' :
            ts = 'Arizona Cardinals'
        elif team_s == 'atl':
            ts = 'Atlanta Falcons'
        elif team_s == 'rav':
            ts = 'Baltimore Ravens'
        elif team_s == 'buf':
            ts = 'Buffalo Bills'
        elif team_s == 'car':
            ts = 'Carolina Panthers'
        elif team_s == 'chi':
            ts = 'Chicago Bears'
        elif team_s == 'cin':
            ts = 'Cincinnati Bengals'
        elif team_s == 'cle':
            ts = 'Cleveland Browns'
        elif team_s == 'dal':
            ts = 'Dallas Cowboys'
        elif team_s == 'den':
            ts = 'Denver Broncos'
        elif team_s == 'det':
            ts = 'Detroit Lions'
        elif team_s == 'gnb':
            ts = 'Green Bay Packers'
        elif team_s == 'htx':
            ts = 'Houston Texans'
        elif team_s == 'clt':
            ts = 'Indianapolis Colts'
        elif team_s == 'jax':
            ts = 'Jacksonville Jaguars'
        elif team_s == 'kan':
            ts = 'Kansas City Chiefs'
        elif team_s == 'mia':
            ts = 'Miami Dolphins'
        elif team_s == 'min':
            ts = 'Minnesota Vikings'
        elif team_s == 'nwe':
            ts = 'New England Patriots'
        elif team_s == 'nor':
            ts = 'New Orleans Saints'
        elif team_s == 'nyg':
            ts = 'New York Giants'
        elif team_s == 'nyj':
            ts = 'New York Jets'
        elif team_s == 'rai':
            ts = 'Oakland Raiders'
        elif team_s == 'phi':
            ts = 'Philadelphia Eagles'
        elif team_s == 'pit':
            ts = 'Pittsburgh Steelers'
        elif team_s == 'sdg':
            ts = 'San Diego Chargers'
        elif team_s == 'sfo':
            ts = 'San Francisco 49ers'
        elif team_s == 'sea':
            ts = 'Seattle Seahawks'
        elif team_s == 'ram':
            ts = 'St. Louis Rams'
        elif team_s == 'stl':
            ts = 'St. Louis Rams'
        elif team_s == 'tam':
            ts = 'Tampa Bay Buccaneers'
        elif team_s == 'oti':
            ts = 'Tennessee Titans'
        elif team_s == 'was':
            ts = 'Washington Redskins'
    except NameError:
        print('Invalid team name')
    return ts

def Full2Abv(team_s):
    try:
        if team_s == 'Arizona Cardinals':
            ts = 'crd'
        elif team_s == 'Atlanta Falcons':
            ts = 'atl'
        elif team_s == 'Baltimore Ravens':
            ts = 'rav'
        elif team_s == 'Buffalo Bills':
            ts = 'buf'
        elif team_s == 'Carolina Panthers':
            ts = 'car'
        elif team_s == 'Chicago Bears':
            ts = 'chi'
        elif team_s == 'Cincinnati Bengals':
            ts = 'cin'
        elif team_s == 'Cleveland Browns':
            ts = 'cle'
        elif team_s == 'Dallas Cowboys':
            ts = 'dal'
        elif team_s == 'Denver Broncos':
            ts = 'den'
        elif team_s == 'Detroit Lions':
            ts = 'det'
        elif team_s == 'Green Bay Packers':
            ts = 'gnb'
        elif team_s == 'Houston Texans':
            ts = 'htx'
        elif team_s == 'Indianapolis Colts':
            ts = 'clt'
        elif team_s == 'Jacksonville Jaguars':
            ts = 'jax'
        elif team_s == 'Kansas City Chiefs':
            ts = 'kan'
        elif team_s == 'Miami Dolphins':
            ts = 'mia'
        elif team_s == 'Minnesota Vikings':
            ts = 'min'
        elif team_s == 'New England Patriots':
            ts = 'nwe'
        elif team_s == 'New Orleans Saints':
            ts = 'nor'
        elif team_s == 'New York Giants':
            ts = 'nyg'
        elif team_s == 'New York Jets':
            ts = 'nyj'
        elif team_s == 'Oakland Raiders':
            ts = 'rai'
        elif team_s == 'Philadelphia Eagles':
            ts = 'phi'
        elif team_s == 'Pittsburgh Steelers':
            ts = 'pit'
        elif team_s == 'San Diego Chargers':
            ts = 'sdg'
        elif team_s == 'San Francisco 49ers':
            ts = 'sfo'
        elif team_s == 'Seattle Seahawks':
            ts = 'sea'
        elif team_s == 'St. Louis Rams':
            ts = 'ram'
        elif team_s == 'Tampa Bay Buccaneers':
            ts = 'tam'
        elif team_s == 'Tennessee Titans':
            ts = 'oti'
        elif team_s == 'Washington Redskins':
            ts = 'was'
    except NameError:
        print('Invalid team name')
    return ts