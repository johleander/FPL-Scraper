import json

def writeToJson(filePath, data):
     with open(filePath, 'w') as f:
        json.dump(data, f)

def appendToJson(filePath, data):
     with open(filePath, 'a') as f:
        json.dump(data, f)

def readAndWriteJson(filePath, data):
     with open(filePath, 'r+') as f:
        json.dump(data, f)

def readFromJson(filePath):
   with open(filePath) as json_file:
      data = json.load(json_file)
      return data