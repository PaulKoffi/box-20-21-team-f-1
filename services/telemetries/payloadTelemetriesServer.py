import requests
import pymongo
from kafka import KafkaConsumer
import json
from bson.json_util import dumps, loads
from time import sleep

BASE_URL = "http://localhost:7000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')
satelliteName = ""

sleep(20)

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='rocket-telemetry-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(['payloadTopic'])


def saveTelemetriesData(satelliteName):
    values = {
        "machine": satelliteName,
        "type": "PAYLOAD",
        "projectionTelemetriesData": []
    }
    db.projectionTelemetriesData.insert_one(values)
    return ""


index = 0

for msg in consumer:
    message = msg.value

    if message['action'] == "running":
        satelliteName = message['payloadName']

        if index == 0:
            saveTelemetriesData(satelliteName)

        myquery = {"satellite": satelliteName}
        projectioValues = json.loads(dumps(db.projectionTelemetriesData.find_one(myquery)))['projectionTelemetriesData']
        projectioValues.append(int(message['state']))

        newvalues = {"$set": {"projectionTelemetriesData": projectioValues}}
        db.projectionTelemetriesData.update_one(myquery, newvalues)
        index += 1

    if message['action'] == "end":
        print("LAST DATA")
        satelliteName = message['payloadName']
        response = requests.get("{}/payload/payloadBySatelliteName/{}".format(BASE_URL, satelliteName))
        if int(response.json()["finalPosition"]) == int(message['state']):
            myobj = {
                "rocketName": str(response.json()["rocketName"]),
                "satelitte": satelliteName
            }
            print(satelliteName)
            x = requests.post("{}/payload/setStatus".format(BASE_URL), json=myobj)
            if x.status_code != 403:
                print("--------------< Satellite mis en Orbite avec succès >------------------")
        else:
            print("ECHEC DE LA MISSION")
        round = 0

    if message['action'] == "destroy":
        print("ECHEC DE LA MISSION")
