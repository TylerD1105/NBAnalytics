from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from fastapi.middleware.cors import CORSMiddleware

DATABASE_URL = "sqlite:///../nba.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    team_id = Column(String, primary_key=True, index=True)
    team_name = Column(String, nullable = False)
    abbreviation = Column(String, nullable = False)
    image_url = Column(String)

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