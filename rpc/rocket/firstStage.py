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

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

time.sleep(10)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='rocket-simulation-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumerDestruction = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='rocket-simulation-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe('launcherTopic')


# consumerDestruction.subscribe(["launcherTopic"])


# def setDestructionValue():
#     print("_____SET_________")
#     global destroy
#     destroy = True


def printAndSendMessages(TOPIC, MESSAGE, rocketNameToSend, siteNameToSend):
    print(MESSAGE)
    data = {'action': MESSAGE,
            'siteName': siteNameToSend,
            'rocketName': rocketNameToSend
            }
    producer.send(TOPIC, value=data)
    time.sleep(1)


for msg in consumer:
    # print("Okay")
    message = msg.value
    if (msg.topic == 'launcherTopic' and message['action'] == const.LAUNCH):
        siteName = message['siteName']
        rocketName = message['rocketName']
        # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
        currentPayload = requests.get(
            "{}/payload/payloadByRocketName/{}".format(const.DELIVERY_STATES_BASE_URL, rocketName))

        # print(currentPayload)

        someRocketStates = json.loads(dumps(db.rocketsStates.find_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": currentPayload.json()["satellite"]})))
        statesArray = someRocketStates["rocketStatesHe"]
        # s = ServerProxy(PAYLOAD_STATES_BASE_URL)

        # Envoi des étapes de lancement de la fusée
        printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_PREPARATION, rocketName, siteName)

        length = len(statesArray)
        for index in range(0, length):
            responseDestruction = requests.get(
                "{}/rocketsStates/destruction/{}/{}".format(const.ROCKETS_STATES_BASE_URL, siteName, rocketName))
            if responseDestruction.text == "True":
                destroy = True
                print("DESTRUCTION")
            if destroy is True:
                print("Rocket destruction!!!!")
                msg = ''
                if index > 10:
                    msg = 'rocket first Stage destruction'

                elif index < 4:
                    msg = 'aborted rocket launching'
                else:
                    msg = 'rocket first Stage , second Stage and payload Destruction'
                data = {'action': "destroy",
                        'siteName': siteName,
                        'rocketName': rocketName,
                        'msg': msg
                        }
                # producer.send(const.ROCKET_TOPIC, value=data)
                producer.send(const.LAUNCHER_TOPIC, value=data)
                producer.send('payloadTopic', value=data)
                producer.send('rocketTopic', value=data)

                stop = True
                break

            if index == 0 and destroy is False:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_ON_INTERNAL_POWER, rocketName, siteName)

            if index == 1 and destroy is False:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_STARTUP, rocketName, siteName)

            if index == 2 and destroy is False:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_MAIN_ENGINE_START, rocketName, siteName)

            if index == 4 and destroy is False:
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_LIFTOFF, rocketName, siteName)
                printAndSendMessages(const.ROCKET_TOPIC, const.LAUNCH, rocketName, siteName)

            if index == 7:
                if destroy is False:
                    printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_MAX_Q, rocketName, siteName)
                    print("Max Q making us reduce the speed to 9")
                    response = requests.put(
                        "{}/rocket/setRocketSpeed/{}/{}".format(const.BASE_URL_ROCKET_INVENTORY, rocketName, 9))
                    time.sleep(5)
                    print("Returning to initial speed")
                    result = requests.put(
                        "{}/rocket/setRocketSpeed/{}/{}".format(const.BASE_URL_ROCKET_INVENTORY, rocketName, 10))
                    printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_MAIN_ENGINE_CUT_OFF, rocketName, siteName)

            if index == 10:
                print(const.ROCKET_SECOND_STAGE_SEPARATION)
                printAndSendMessages(const.LAUNCHER_TOPIC, const.ROCKET_SECOND_STAGE_SEPARATION, rocketName, siteName)

            time.sleep(4)

            if index > 4 and index != length - 1:
                data = {'action': const.RUNNING,
                        'siteName': siteName,
                        'rocketName': rocketName,
                        'state': str(statesArray[index])}
                producer.send('rocketTopic', value=data)

            if index == 11:
                printAndSendMessages(const.LAUNCHER_TOPIC, "Flip maneuver", rocketName, siteName)
                printAndSendMessages("testTopic", "Flip maneuver", rocketName, siteName)

            if index == 12:
                printAndSendMessages(const.LAUNCHER_TOPIC, "Entry burn", rocketName, siteName)
                printAndSendMessages("testTopic", "Entry burn", rocketName, siteName)

            if index == 13:
                printAndSendMessages(const.LAUNCHER_TOPIC, "Guidance", rocketName, siteName)
                printAndSendMessages("testTopic", "Guidance", rocketName, siteName)

            if index == 14:
                printAndSendMessages(const.LAUNCHER_TOPIC, "Landing burn", rocketName, siteName)
                printAndSendMessages("testTopic", "Landing burn", rocketName, siteName)

            if index == 15:
                printAndSendMessages(const.LAUNCHER_TOPIC, "Landing legs deployed", rocketName, siteName)
                printAndSendMessages("testTopic", "Landing legs deployed", rocketName, siteName)

            # if index == 16:

            if index == length - 1:
                data = {'action': "end",
                        'siteName': siteName,
                        'rocketName': rocketName,
                        'state': str(statesArray[index])}
                producer.send('rocketTopic', value=data)

        if stop is False:
            print("Rocket at the end of the launch")

        destroy = False
        # MAJ du statut de la mission (PAST)
        myobj = {
            "rocketName": rocketName
        }
        requests.post("{}/payload/setPastMissionValue".format(const.DELIVERY_STATES_BASE_URL), json=myobj)
        if not stop:
            printAndSendMessages(const.LAUNCHER_TOPIC, "Landing", rocketName, siteName)
            printAndSendMessages("testTopic", "Landing", rocketName, siteName)
        stop = False
        print(
            "_______________________________________________________________________________________________________________________")
        print("\n")

    # if (msg.topic == LAUNCHER_TOPIC and message['action'] == ROCKET_DESTRUCTION):
    #     destroy = True
