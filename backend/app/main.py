from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent        # backend/app
DATABASE_URL = f"sqlite:///{(BASE_DIR.parent / 'nba.db')}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    team_id = Column(String, primary_key=True, index=True)
    team_name = Column(String, nullable = False)
    abbreviation = Column(String, nullable = False)
    image_url = Column(String)
    #Add more stats for teams, or, make individual Team-Stats table that will link



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/teams")
async def read_teams():
    db = sessionLocal()
    teams = db.query(Team).all()
    result = [
        {
            "team_id": t.team_id,
            "team_name": t.team_name,
            "abbreviation": t.abbreviation,
            "image_url": t.image_url
        }
        for t in teams
    ]
    db.close()
    return result




#Next step is to create another class and database where it will us

class TeamStats(Base):
    __tablename__ = "team_stats"
    team_id = Column(String, primary_key=True, index=True)
    wins = Column(Integer)
    losses = Column(Integer)
    points_per_game = Column(Float)
    rebounds_per_game = Column(Float)
    assists_per_game = Column(Float)
    conference_standing = Column(Integer)
    div_standing = Column(Integer)
    # Add more stats as needed


Base.metadata.create_all(bind=engine)

@app.post("/team-stats/{team_id}/sync-stats")
async def sync_team_stats(team_id: str):
    from TeamStatFunction import fetch_team_stats
    stats = fetch_team_stats(team_id)
    db = sessionLocal()
    db.merge(stats)
    db.commit()
    db.close()

@app.post("/team-stats/sync-all")
async def sync_all_team_stats():
    from TeamStatFunction import fetch_team_stats
    import time
    db = sessionLocal()
    teams = db.query(Team).all()
    results = []
    for team in teams:
        try:
            stats = fetch_team_stats(team.team_id)
            db.merge(TeamStats(team_id=team.team_id, **stats))
            results.append({"team_id": team.team_id, "team_name": team.team_name, "status": "success"})
            time.sleep(0.5)  # To avoid hitting API rate limits
        except Exception as e:
            results.append({"team_id": team.team_id, "team_name": team.team_name, "status": f"error: {str(e)}"})
    db.commit()
    db.close()
    return results

@app.get("/team-stats/{team_id}")
async def get_team_stats(team_id: str):
    db = sessionLocal()
    stats = db.query(TeamStats).filter(TeamStats.team_id == team_id).first()
    result =  {
        "team_id": stats.team_id,
        "wins": stats.wins,
        "losses": stats.losses,
        "points_per_game": stats.points_per_game,
        "rebounds_per_game": stats.rebounds_per_game,
        "assists_per_game": stats.assists_per_game,
        "conference_standing": stats.conference_standing,
        "div_standing": stats.div_standing
    }
    db.close()
    return result