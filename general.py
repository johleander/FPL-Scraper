from asyncio import constants
import get_data
import pandas as pd
import numpy as np
import constants as fpl_consts


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
get_data.get_team_data(fpl_consts.MY_FPL_MANAGER_ID , True)

#GET TEAM HISTORY DATA
get_data.get_team_history_data(fpl_consts.MY_FPL_MANAGER_ID, True)

#GET TEAM TRANSFERS 
get_data.get_team_transfers_data(fpl_consts.MY_FPL_MANAGER_ID, True)

#GET SQUAD PICKS FOR ME 

for x in range(38):
    get_data.squad_picks(fpl_consts.MY_FPL_MANAGER_ID,x+1, True)


