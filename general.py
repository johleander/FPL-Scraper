from asyncio import constants
import get_data
import pandas as pd
import numpy as np


generalData = get_data.get_main_data(True)
elements_df = pd.DataFrame(generalData['elements'])


#idName_df = elements_df[["id", "first_name", "second_name"]]

#GET ALL ELEMENTS

for index, row in elements_df.iterrows():
    id = row["id"]
    name = row["first_name"]+"_"+row["second_name"]
    get_data.get_element_data(id,name, True)

#GET FIXTURES 
get_data.get_fixtures(True)

#GET GAMEWEEK DATA  
get_data.get_gameweek_data()

#GET TEAM DATA 
get_data.get_team_data(1110439, True)

#GET TEAM HISTORY DATA
get_data.get_team_history_data(1110439, True)

#GET TEAM TRANSFERS 
get_data.get_team_transfers_data(1110439, True)

#GET SQUAD PICKS FOR ME 

for x in range(38):
    get_data.squad_picks(1110439,x+1, True)


#GET LEAGUE STANDINGS FOR STÅNGBY LEAGUE
data = get_data.league_standings(227667, 1)

