from flask import jsonify
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
import json

class RocketStatesResource():
    



    def getSecondStepByNameAndSite(self,siteName,rocketName):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)


        client = pymongo.MongoClient(
        "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
        db = client.get_database('blueOrigin')
        rocketAction=json.loads(dumps(db.rocketActions.find_one({"rocketName": rocketName, "siteName": siteName})))
        return str(rocketAction["secondStep"])

    def getDestructionByNameAndSite(self,siteName,rocketName):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)


        client = pymongo.MongoClient(
        "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
        db = client.get_database('blueOrigin')
        rocketAction=json.loads(dumps(db.rocketActions.find_one({"rocketName": rocketName, "siteName": siteName})))
        return str(rocketAction["stopLaunching"])

    def getLaunchingByNameAndSite(self,siteName,rocketName):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)


        client = pymongo.MongoClient(
        "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
        db = client.get_database('blueOrigin')
        rocketAction=json.loads(dumps(db.rocketActions.find_one({"rocketName": rocketName, "siteName": siteName})))
        print(str(rocketAction["launch"]))
        return str(rocketAction["launch"])

    def putSecondStepByNameAndSite(self,siteName,rocketName,newState):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        client = pymongo.MongoClient(
        "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
        db = client.get_database('blueOrigin')
        db.rocketActions.update_one({"rocketName": rocketName, "siteName": siteName}, {'$set': {'secondStep': bool(newState)}})
        return "done"

    def putDestructionByNameAndSite(self,siteName,rocketName,newState):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)


        client = pymongo.MongoClient(
        "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
        db = client.get_database('blueOrigin')
        db.rocketActions.update_one({"rocketName": rocketName, "siteName": siteName}, {'$set': {'stopLaunching': bool(newState)}})
        return "done"

    def putLaunchingByNameAndSite(self,siteName,rocketName,newState):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        client = pymongo.MongoClient(
        "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
        db = client.get_database('blueOrigin')
        db.rocketActions.update_one({"rocketName": rocketName, "siteName": siteName}, {'$set': {'launch': bool(newState)}})
        return "done"