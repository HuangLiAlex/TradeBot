import json


def parseCNSTK(rawData):
    jsonData = rawData.to_json(orient='records', lines=True)
    jsonDataList = jsonData.splitlines()

    jsonObject = {}
    for i in range(len(jsonDataList)):
        line = jsonDataList[i]
        jsonObject[i] = line

    return json.loads(json.dumps(jsonObject))
