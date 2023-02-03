
import requests
import constants
from jsonParser import writeToJson
import os

dirname = os.path.dirname(__file__)
responsesYear = "data/2022-23"

def get_data(url): 
    response = requests.get(url)

    if(response.status_code == 200):
        data = response.json()
        return data
    else: 
        return "You got an error with code: " +response.status_code

def get_main_data(saveResponse = False):
    print("Fetching main data")
    url = constants.MAIN_DATA_URL
    data = get_data(url)
    
    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/general.json"), data)
    return data

def get_fixtures(saveResponse = False):
    print("Fetching fixtures")
    url = constants.FIXTURES_URL
    data =  get_data(url)

    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/fixtures.json"), data)
    return data
    
def get_gameweek_data():
    print("Fetching gameweek data")
    url = constants.GAMEWEEK_URL

    for x in range(38):
        gw_url = url.format(x+1)
        data =  get_data(gw_url)
        writeToJson(os.path.join(dirname, f"./{responsesYear}/GW/gw{x+1}.json"), data)
         


def get_team_data(teamId, saveResponse = False):
    print("Fetching team data")
    url = constants.TEAM_URL
    team_url = url.format(teamId)
    data = get_data(team_url)

    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/team.json"), data)
    return data

def get_team_history_data(teamId, saveResponse = False):
    print("Fetching team history data")
    url = constants.TEAM_HISTORY_URL
    team_history_url = url.format(teamId)
    data = get_data(team_history_url)

    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/team_history.json"), data)
    return data

def get_team_transfers_data(teamId, saveResponse = False):
    print("Fetching team transfers")
    url = constants.TEAM_TRANSFERS_URL
    team_transfers_url = url.format(teamId)
    data = get_data(team_transfers_url )

    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/team_transfers.json"), data)
    return data



def squad_picks(teamId, gw, saveResponse = False):
    print("Fetching squad picks for gw: " + str(gw))
    url = constants.TEAM_GAMEWEEK_PICKS_URL
    picks_url = url.format(teamId, gw)
    data = get_data(picks_url)
    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/GW/my_gw_{gw}.json"), data)
    return data

def league_standings(leagueId, page = 1, saveResponse = False):
    print("Fetching league standings")
    url = constants.LEAGUE_STANDINGS_URL
    standings_url = url.format(leagueId, page)
    data = get_data(standings_url)
    leagueIdStr = str(leagueId)
    if(saveResponse):
        writeToJson(os.path.join(dirname, f"./{responsesYear}/league_{leagueIdStr}.json"), data)
    return data

def get_element_data(elementId, fileName, saveResponse = False):
    print("Fetching element data for: " + str(elementId))
    url = constants.ELEMENT_SUMMARY_URL
    element_url = url.format(elementId)
    data = get_data(element_url)
    if(saveResponse):
        name = str(elementId)+"_"+fileName
        writeToJson(os.path.join(dirname, f"./{responsesYear}/Elements/{name}.json"), data)
    return data

