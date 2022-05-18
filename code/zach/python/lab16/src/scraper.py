import requests

def regular_season(season, seasonType):
    reqUrl = f"https://site.web.api.espn.com/apis/common/v3/sports/football/nfl/statistics/byteam?region=us&lang=en&contentorigin=espn&sort=team.returning.yardsPerKickReturn%3Adesc&limit=32&season={ season }&seasontype={ seasonType }"

    headersList = {
    "Accept": "*/*",
    }

    payload = ""

    response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

    print(response.text)



regular_season(2011, 2)