from datetime import datetime

from app.endpoints.match import Match


def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


FIXTURES = [
    {
        "id": 1,
        "home_team": "FC Liverpool",
        "away_team": "Chelsea",
        "date": "2018-09-29 16:00",
    },
    {
        "id": 2,
        "home_team": "Arsenal",
        "away_team": "Manchester City",
        "date": "2018-09-29 18:00"
    },
    {
        "id": 3,
        "home_team": "West Ham United",
        "away_team": "Manchester United",
        "date": "2018-09-30 15:00"
    }
]


def read():
    return FIXTURES


class Fixture(Match):
    def __init__(self, home_team, away_team, date):
        super().__init__(self, home_team, away_team, date)


