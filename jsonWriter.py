import json

def writeToJson(filePath, data):
     with open(filePath, 'w') as f:
        json.dump(data, f)