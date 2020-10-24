from flask import jsonify
import pymongo
from datetime import datetime
import requests
from pymongo import MongoClient
from bson.json_util import dumps, loads
import json

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


class EventRegistrationResource():

    def getLogBySatelliteName(self, satelliteName):
        return json.loads(dumps(db.logEvent.find(
            {'satelliteName': satelliteName})))

    def addLog(self, rocketName, siteName, satelliteName, message):
        db.logEvent.insert_one({
            "rocketName": rocketName,
            "siteName": siteName,
            "satelliteName": satelliteName,
            "message": message,
            "date": datetime.now()
        })
        return 'success', 200
