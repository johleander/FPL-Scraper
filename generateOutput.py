import json
import os
import pandas as pd
from os.path import exists
from jsonParser import readFromJson, writeToJson

def convertToTeamName(teams_df,id):
 
    team = teams_df.loc[teams_df["id"] == id]
    return team["name"].values[0]


dirname = os.path.dirname(__file__)
years = ["2021-22", "2022-23"]
players = []

excluded_elements_columns = [
     "cost_change_event",
     "cost_change_event_fall",
     "cost_change_start",
     "cost_change_start_fall",
     "special"
    ]


for year in years:
    players = []
    
    path = os.path.join(dirname, f"./data/{year}/Elements")
    general_data = readFromJson(f"./data/{year}/general.json")
    elements_df = pd.DataFrame(general_data['elements'])
    teams_df = pd.DataFrame(general_data['teams'])
 
    elements_subset_df = elements_df.loc[:, ~elements_df.columns.isin(excluded_elements_columns)]
  

    for filename in os.listdir(path):
        f = os.path.join(path,filename)
        if os.path.isfile(f) and filename.endswith(".json"):
            data = readFromJson(f)
            history = data["history"]
            #Find item from elements
            if len(history) > 0:
                element = elements_subset_df.loc[elements_subset_df["id"] ==  history[0]["element"]]
                element.fillna("", inplace=True)
                team = convertToTeamName(teams_df,element.team.values[0])
        
                outputName = str(element.code.values[0])
                outputFile = os.path.join(dirname, f"output/{outputName}.json")
                playerElement = (element.to_dict(orient = "records")[0])
                playerElement["season"] = year
                playerElement["team"] = convertToTeamName(teams_df, playerElement["team"] )
                playerElement["history"] = history
                

                for pe in playerElement["history"]:
                    pe["opponent_team"] = convertToTeamName(teams_df, pe["opponent_team"])
             
                file_exists = os.path.exists(os.path.join(dirname, f"output/{outputName}.json"))
                data = {}
                if file_exists:
                    with open(outputFile, 'r') as json_file:
                        print("Exists")
                        data = json.load(json_file)
                        data["team"] = team
                        data["seasons"].append(playerElement)
                else:
                    data =  {
                        "id": str(element.code.values[0]),
                        "name": str(element.first_name.values[0]) + " " + str(element.second_name.values[0]),
                        "type": "player", 
                        "team": team, 
                        "seasons": []
                    }   
                    data["seasons"].append(playerElement)
                    print("Do not Exists")
                    
                with open(outputFile, 'w') as json_file:
                    json.dump(data,json_file)




              
               
                
                        
                   
               

        






        