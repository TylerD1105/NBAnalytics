from main import Team, sessionLocal

teams = [
    {"team_id": "ATL", "team_name": "Atlanta Hawks", "abbreviation": "ATL", "image_url": "/images/teams/ATL.png"},
    {"team_id": "BOS", "team_name": "Boston Celtics", "abbreviation": "BOS", "image_url": "/images/teams/BOS.png"},
    {"team_id": "BKN", "team_name": "Brooklyn Nets", "abbreviation": "BKN", "image_url": "/images/teams/BKN.png"},
    {"team_id": "CHA", "team_name": "Charlotte Hornets", "abbreviation": "CHA", "image_url": "/images/teams/CHA.png"},
    {"team_id": "CHI", "team_name": "Chicago Bulls", "abbreviation": "CHI", "image_url": "/images/teams/CHI.png"},
    {"team_id": "CLE", "team_name": "Cleveland Cavaliers", "abbreviation": "CLE", "image_url": "/images/teams/CLE.png"},
    {"team_id": "DAL", "team_name": "Dallas Mavericks", "abbreviation": "DAL", "image_url": "/images/teams/DAL.png"},
    {"team_id": "DEN", "team_name": "Denver Nuggets", "abbreviation": "DEN", "image_url": "/images/teams/DEN.png"},
]


db = sessionLocal()
for t in teams:
    team = Team(**t)
    db.merge(team)
db.commit()
db.close()