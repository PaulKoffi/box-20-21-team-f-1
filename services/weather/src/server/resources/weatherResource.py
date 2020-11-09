# import pymongo
import json
from json import dumps, loads

# from pymongo import MongoClient
# from bson.json_util import dumps, loads

# client = pymongo.MongoClient(
#     "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
# db = client.get_database('blueOrigin')

sites = [
    {
        "name": "Rennes",
        "humidity": 9,
        "rainPrecipitation": 3,
        "temperature": 7,
        "wind": 9
    },
    {
        "name": "Nice",
        "humidity": 9,
        "rainPrecipitation": 3,
        "temperature": 7,
        "wind": 9
    },
    {
        "name": "Paris",
        "humidity": 9,
        "rainPrecipitation": 3,
        "temperature": 7,
        "wind": 9
    },
    {
        "name": "Toulouse",
        "humidity": 12,
        "rainPrecipitation": 3,
        "temperature": 7,
        "wind": 11
    }
]


class WeatherResource():
    def getAllSites(self):
        response = json.loads(dumps(sites))
        # print(response)
        return response

    def getSiteByName(self, siteName):
        for site in sites:
            if site['name'] == siteName:
                return json.loads(dumps(site))

    # def setRocketStatus(self, id):
    #     myquery = {"rocketName": id}
    #     newvalues = {"$set": {"available": True}}
    #     db.rocketinventories.update_one(myquery, newvalues)
    #     return json.loads(dumps(db.rocketinventories.find_one({"rocketName": id})))

    # def setRocketSpeed(self, id, speed):
    #     myquery = {"rocketName": id}
    #     actuelSpeed = json.loads(dumps(db.rocketinventories.find_one(myquery)))["speed"]
    #     newvalues = {"$set": {"speed": speed}}
    #     db.rocketinventories.update_one(myquery, newvalues)
    #     return str(actuelSpeed)
