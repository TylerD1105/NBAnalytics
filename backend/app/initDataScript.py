from main import Team, sessionLocal
from nba_api.stats.static import teams
teamList = [
    {"team_id": "ATL", "team_name": "Atlanta Hawks", "abbreviation": "ATL", "image_url": "/images/teams/ATL.png"},
    {"team_id": "BOS", "team_name": "Boston Celtics", "abbreviation": "BOS", "image_url": "/images/teams/BOS.png"},
    {"team_id": "BKN", "team_name": "Brooklyn Nets", "abbreviation": "BKN", "image_url": "/images/teams/BKN.png"},
    {"team_id": "CHA", "team_name": "Charlotte Hornets", "abbreviation": "CHA", "image_url": "/images/teams/CHA.png"},
    {"team_id": "CHI", "team_name": "Chicago Bulls", "abbreviation": "CHI", "image_url": "/images/teams/CHI.png"},
    {"team_id": "CLE", "team_name": "Cleveland Cavaliers", "abbreviation": "CLE", "image_url": "/images/teams/CLE.png"},
    {"team_id": "DAL", "team_name": "Dallas Mavericks", "abbreviation": "DAL", "image_url": "/images/teams/DAL.png"},
    {"team_id": "DEN", "team_name": "Denver Nuggets", "abbreviation": "DEN", "image_url": "/images/teams/DEN.png"},
    {"team_id": "DEN", "team_name": "Detroit Pistons", "abbreviation": "DET", "image_url": "/images/teams/DET.png"},
    {"team_id": "DEN", "team_name": "Golden State Warriors", "abbreviation": "GSW", "image_url": "/images/teams/GSW.png"},
    {"team_id": "DEN", "team_name": "Houston Rockets", "abbreviation": "HOU", "image_url": "/images/teams/HOU.png"},
    {"team_id": "DEN", "team_name": "Indiana Pacers", "abbreviation": "IND", "image_url": "/images/teams/IND.png"},
    {"team_id": "DEN", "team_name": "Los Angeles Clippers", "abbreviation": "LAC", "image_url": "/images/teams/LAC.png"},
    {"team_id": "DEN", "team_name": "Los Angeles Lakers", "abbreviation": "LAL", "image_url": "/images/teams/LAL.png"},
    {"team_id": "DEN", "team_name": "Memphis Grizzlies", "abbreviation": "MEM", "image_url": "/images/teams/MEM.png"},
    {"team_id": "DEN", "team_name": "Miami Heat", "abbreviation": "MIA", "image_url": "/images/teams/MIA.png"},
    {"team_id": "DEN", "team_name": "Milwaukee Bucks", "abbreviation": "MIL", "image_url": "/images/teams/MIL.png"},
    {"team_id": "DEN", "team_name": "Minnesota Timberwolves", "abbreviation": "MIN", "image_url": "/images/teams/MIN.png"},
    {"team_id": "DEN", "team_name": "New Orleans Pelicans", "abbreviation": "NOP", "image_url": "/images/teams/NOP.png"},
    {"team_id": "DEN", "team_name": "New York Knicks", "abbreviation": "NYK", "image_url": "/images/teams/NYK.png"},
    {"team_id": "DEN", "team_name": "Oklahoma City Thunder", "abbreviation": "OKC", "image_url": "/images/teams/OKC.png"},
    {"team_id": "DEN", "team_name": "Orlando Magic", "abbreviation": "ORL", "image_url": "/images/teams/ORL.png"},
    {"team_id": "DEN", "team_name": "Philadelphia 76ers", "abbreviation": "PHI", "image_url": "/images/teams/PHI.png"},
    {"team_id": "DEN", "team_name": "Phoenix Suns", "abbreviation": "PHX", "image_url": "/images/teams/PHO.png"},
    {"team_id": "DEN", "team_name": "Portland Trail Blazers", "abbreviation": "POR", "image_url": "/images/teams/POR.png"},
    {"team_id": "DEN", "team_name": "Sacramento Kings", "abbreviation": "SAC", "image_url": "/images/teams/SAC.png"},
    {"team_id": "DEN", "team_name": "San Antonio Spurs", "abbreviation": "SAS", "image_url": "/images/teams/SAS.png"},
    {"team_id": "DEN", "team_name": "Toronto Raptors", "abbreviation": "TOR", "image_url": "/images/teams/TOR.png"},
    {"team_id": "DEN", "team_name": "Utah Jazz", "abbreviation": "UTA", "image_url": "/images/teams/UTA.png"},
    {"team_id": "DEN", "team_name": "Washington Wizards", "abbreviation": "WAS", "image_url": "/images/teams/WAS.png"}

]


#Need to call NBA API to set the true team_id in terms as to what the API says the Team_ID is, can create a function to do that.
for t in teamList:
    teamId = teams.find_team_by_abbreviation(t["abbreviation"]) 
    if teamId:
        t["team_id"] = teamId["id"]


db = sessionLocal()
for t in teamList:
    team = Team(**t)
    db.merge(team)
db.commit()
db.close()