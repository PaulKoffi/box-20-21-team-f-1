from flask import jsonify
import pymongo
import json
from pymongo import MongoClient
from bson.json_util import dumps, loads

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


class SatelliteResource():
    def getAllSatellites(self):
        response = json.loads(dumps(db.satellite.find()))
        # print(response)
        return jsonify(response)

    def getSatelliteById(self, id):
        return jsonify(json.loads(dumps(db.satellite.find_one({"satelliteName": id}))))

    def setSatelliteFuel(self, id, fuelToAdd):
        myquery = {"satelliteName": id}
        newvalues = {"$inc": {"fuel": fuelToAdd}}
        db.satellite.update_one(myquery, newvalues)
        return jsonify(json.loads(dumps(db.satellite.find_one({"satelliteName": id}))))

