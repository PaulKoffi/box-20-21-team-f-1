from flask import jsonify
import pymongo
import requests
from pymongo import MongoClient
from bson.json_util import dumps, loads
import json

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


# def getCurrentSatelliteName(rocketName):
#     DELIVERY_STATES_BASE_URL = "http://localhost:7000"
#     # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
#     currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
#     print("\n-----------------\n")
#     print(currentPayload)
#     print("\n-----------------\n")
#     return currentPayload.json()["satellite"]


class DeliveryResource():

    def getPayloadByRocketName(self, rocketName):
        return json.loads(dumps(db.payloads.find_one(
            {"rocketName": rocketName})))

    def getPayloadBySatelliteName(self, satelliteName):
        return json.loads(dumps(db.payloads.find_one(
            {'satellite': satelliteName})))

    def setPastMissionValue(self, rocketName):
        print("________________________________________________")
        db.payloads.update_one(
            {"rocketName": rocketName},
            {'$set': {"past": True}})
        return 'success', 200

    def addPayload(self, customerName, customerMail, finalPosition, x, y, satellite):
        rocketsAvailable = json.loads(dumps(db.rocketinventories2.find_one(
            {"available": True})))

        clientFound = json.loads(dumps(db.customers.find_one(
            {'mail': customerMail})))

        # print("R")
        # print(rocketsAvailable)

        if clientFound is None:
            db.customers.insert_one({
                "name": customerName,
                "mail": customerMail
            })

        if rocketsAvailable is not None:
            db.payloads.insert_one({
                "customer": customerMail,
                "rocketName": rocketsAvailable["rocketName"],
                "finalPosition": finalPosition,
                "position": [str(x), str(y)],
                "satellite": satellite,
                "success": False,
                "past": False
            })

            # db.rocketinventories2.update_one(
            #     {"rocketName": rocketsAvailable["rocketName"]},
            #     {'$set': {"available": False}})

            return json.loads(dumps(db.payloads.find_one(
                {'satellite': satellite})))

        return 'failed', 403

    def setStatus(self, rocketName, satellite):
        result = json.loads(dumps(db.payloads.find_one(
            {"rocketName": rocketName, "satellite": satellite})))
        success = result["success"]
        res = True
        if success:
            res = False
        print("----------------")
        print(res)
        db.payloads.update_one(
            {"rocketName": rocketName},
            {'$set': {"success": res}})
        return 'success', 200
