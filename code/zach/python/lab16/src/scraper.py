import requests
import pandas as pd

def regular_season(season, seasonType):
    url = f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/statistics/byteam?region=us&lang=en&contentorigin=espn&sort=team.returning.yardsPerKickReturn%3Adesc&limit=32&season={ season }&seasontype={ seasonType }"

    headersList = {
    "Accept": "*/*",
    }

    r = requests.get(url,  headers=headersList)
    season_data = r.json()
    df = pd.json_normalize(season_data['teams'])
    df.to_csv('season_data.csv', index=False)

x = regular_season(2011, 2)