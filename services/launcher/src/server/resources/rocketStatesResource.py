from flask import jsonify
import pymongo
import requests
from pymongo import MongoClient
from bson.json_util import dumps, loads
import json

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


def getCurrentSatelliteName(rocketName):
    DELIVERY_STATES_BASE_URL = "http://localhost:7000"
    # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
    currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
    print("\n-----------------\n")
    print(currentPayload)
    print("\n-----------------\n")
    return currentPayload.json()["satellite"]


class RocketStatesResource():

    def getSecondStepByNameAndSite(self, siteName, rocketName):
        satellite = getCurrentSatelliteName(rocketName)
        rocketAction = json.loads(dumps(db.rocketActions.find_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": satellite})))
        return str(rocketAction["secondStep"])

    def getDestructionByNameAndSite(self, siteName, rocketName):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        satellite = getCurrentSatelliteName(rocketName)

        rocketAction = json.loads(dumps(db.rocketActions.find_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": satellite})))
        return str(rocketAction["stopLaunching"])

    def getLaunchingByNameAndSite(self, siteName, rocketName):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        satellite = getCurrentSatelliteName(rocketName)
        rocketAction = json.loads(dumps(db.rocketActions.find_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": satellite})))
        return str(rocketAction["launch"])

    def putSecondStepByNameAndSite(self, siteName, rocketName, newState):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        satellite = getCurrentSatelliteName(rocketName)

        db.rocketActions.update_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": satellite},
            {'$set': {'secondStep': bool(newState)}})
        return "done"

    def putDestructionByNameAndSite(self, siteName, rocketName, newState):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        satellite = getCurrentSatelliteName(rocketName)

        db.rocketActions.update_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": satellite},
            {'$set': {'stopLaunching': bool(newState)}})
        return "done"

    def putLaunchingByNameAndSite(self, siteName, rocketName, newState):
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
        PORT = 5353  # Port to listen on (non-privileged ports are > 1023)
        satellite = getCurrentSatelliteName(rocketName)

        db.rocketActions.update_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": satellite},
            {'$set': {'launch': bool(newState)}})
        return "done"
