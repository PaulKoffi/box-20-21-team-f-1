import requests
import pymongo
from kafka import KafkaConsumer
import json
from bson.json_util import dumps, loads
from time import sleep

BASE_URL = "http://localhost:8000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')
rocketName = ""

sleep(5)

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='rocket-telemetry-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(['rocketTopic'])


def getCurrentSatelliteName(rocketName):
    DELIVERY_STATES_BASE_URL = "http://localhost:7000"
    # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
    currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
    return currentPayload.json()["satellite"]


def saveTelemetriesData(rocketName):
    values = {
        "machine": rocketName,
        "type": "ROCKET",
        "projectionTelemetriesData": [],
        "satellite": getCurrentSatelliteName(rocketName)
    }
    db.projectionTelemetriesData.insert_one(values)


index = 0

for msg in consumer:
    message = msg.value
    if (message['action'] == "running"):
        rocketName = message['rocketName']
        
        if index == 0:
            saveTelemetriesData(rocketName)

        myquery = {"satellite": getCurrentSatelliteName(rocketName)}
        projectioValues = json.loads(dumps(db.projectionTelemetriesData.find_one(myquery)))['projectionTelemetriesData']
        projectioValues.append(int(message['state']))

        newvalues = {"$set": {"projectionTelemetriesData": projectioValues}}
        db.projectionTelemetriesData.update_one(myquery, newvalues)
        index += 1

    # if destruction
    if message['action'] == "destroy":
        print("DESTRUCTION")

        rocketName = message['rocketName']
        index = 0
        myobj = {
            "rocketName": rocketName
        }
        x = requests.post("{}/payload/setStatus".format(BASE_URL), data=myobj)

    if message['action'] == "end":
        rocketName = message['rocketName']
        print("LAST DATA ")
        print(message['state'])
        if 0 == int(message['state']):
            print("--------------< La rocket a atteri avec succès  >------------------")
            # Rendre la rocket à nouveau disponible
            # response = requests.post("{}/rocket/setStatus/{}".format(BASE_URL, rocketName))
            # if response.status_code == 403:
            #     print(" ERREUR !")
            # else:
            #     print(" La rocket {} est de nouveau disponible pour une mission !".format(rocketName))
        else:
            print("La rocket est endommagée !!")
        index = 0
