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

Base.metadata.create_all(bind=engine)

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

@app.post("/team-stats/{team_id}/sync-stats")
async def sync_team_stats(team_id: str):
    from TeamStatFunction import fetch_team_stats
    stats = fetch_team_stats(team_id)
    db = sessionLocal()
    db.merge(stats)
    db.commit()
    db.close()