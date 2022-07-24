import json
import requests


def fetch(endpoint):
    api_base = "https://johleander-api.azurewebsites.net/api/football/"
    response_api = requests.get(api_base + endpoint)

    if(response_api.status_code == 200):
        data = response_api.text
        parse_json=json.loads(data)
        return parse_json
    else: 
        return "You got an error with code: " +response_api.status_code
