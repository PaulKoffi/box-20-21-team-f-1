from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
from xmlrpc.client import ServerProxy
from kafka import KafkaConsumer
from kafka import KafkaProducer
import constants as const

destroy = False
stop = False

# secondStageStatesHe

rocket = SimpleXMLRPCServer(('localhost', 8888), logRequests=True, allow_none=True)

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='secondstage-simulation-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumerDestruction = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='secondstage-destruction-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe([const.LAUNCHER_TOPIC])

consumerDestruction.subscribe([const.LAUNCHER_TOPIC])


def printAndSendMessages(TOPIC, MESSAGE, rocketNameToSend, siteNameToSend):
    print(MESSAGE)
    data = {'action': MESSAGE,
            'siteName': siteNameToSend,
            'rocketName': rocketNameToSend
            }
    producer.send(TOPIC, value=data)
    time.sleep(1)


for msg in consumer:
    message = msg.value
    if message['action'] == const.ROCKET_SECOND_STAGE_SEPARATION:
        siteName = message['siteName']
        rocketName = message['rocketName']
        # secondStageName = message['secondStageName']
        # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
        currentPayload = requests.get(
            "{}/payload/payloadByRocketName/{}".format(const.DELIVERY_STATES_BASE_URL, rocketName))
        print("----------------------- ICI --------------------------------------")
        someRocketStates = json.loads(dumps(db.rocketsStates.find_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": currentPayload.json()["satellite"]})))
        statesArray = someRocketStates["secondStageStatesHe"]

        length = len(statesArray)
        for index in range(0, length):
            if index == 0:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_SECOND_ENGINE_START, rocketName, siteName)

            if index == 1:
                # print(const.STAGE_SEPARATION)
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_SECOND_STAGE_SEPARATION, rocketName, siteName)

            if index == 2:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_SECOND_ENGINE_START, rocketName, siteName)

            if index == 3:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_FAIRING_SEPARATION, rocketName, siteName)

            if index == 4:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_SECOND_ENGINE_CUT_OFF, rocketName, siteName)

            if index == 5:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.PAYLOAD_SEPARATION, rocketName, siteName)

            time.sleep(4)

            data = {'action': const.RUNNING,
                    'siteName': siteName,
                    # 'secondStageName': secondStageName,
                    'rocketName': rocketName,
                    'state': str(statesArray[index])}
            producer.send('rocketTopic', value=data)

            if index == length - 1:
                data = {'action': "Seconde Stage destruction",
                        'siteName': siteName,
                        'rocketName': rocketName,
                        # 'secondStageName': secondStageName,
                        'state': str(statesArray[index])}
                producer.send('rocketTopic', value=data)

        stop = False
        destroy = False
        # MAJ du statut de la mission (PAST)
        myobj = {
            "rocketName": rocketName
        }
        requests.post("{}/payload/setPastMissionValue".format(const.DELIVERY_STATES_BASE_URL), data=myobj)

    # if (msg.topic == LAUNCHER_TOPIC and message['action'] == ROCKET_DESTRUCTION):
    #     destroy = True

for msg in consumerDestruction:
    message = msg.value
    if (msg.topic == 'launcherTopic' and message['action'] == const.ROCKET_DESTRUCTION):
        destroy = True
