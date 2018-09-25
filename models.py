from flask import logging
from sqlalchemy import Column, DateTime, String, create_engine
from server import init_db

logging.basicConfig(level=logging.INFO)
db_session = init_db('sqlite:///:memory:')


class Fixture(Base):
    __tablename__ = 'fixtures'
    id = Column(String(20), primary_key=True)
    home_team = Column(String(100))
    away_team = Column(String(100))
    played_at = Column(DateTime())
    created_at = Column(DateTime())
    
    def __init__(self, home_team, away_team, played_at):
        self.home_team, self.away_team, self.played_at = home_team, away_team, played_at

    def create(self):
        self

