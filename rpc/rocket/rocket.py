# from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
# import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
# from xmlrpc.client import ServerProxy
from kafka import KafkaConsumer
from kafka import KafkaProducer


# HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
# PORT = 9490  # Port to listen on (non-privileged ports are > 1023)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
PAYLOAD_STATES_BASE_URL = "http://localhost:8282"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
DELIVERY_STATES_BASE_URL = "http://localhost:7000"
LAUNCH = "launch"
STAGE_SEPARATION = "Stage separation"
ROCKET_DESTRUCTION = "destroy"
ROCKET_TOPIC = "rocketTopic"
LAUNCHER_TOPIC = "launcherTopic"
RUNNING = "running"
ROCKET_PREPARATION = "Rocket preparation"
ROCKET_ON_INTERNAL_POWER = "Rocket on internal power"
ROCKET_STARTUP = "Startup"
ROCKET_MAIN_ENGINE_START = "Main engine start"
ROCKET_LIFTOFF = "Liftoff"
ROCKET_MAX_Q = "Max Q"
ROCKET_MAIN_ENGIE_CUT_OFF = "Main engine cut-off"
ROCKET_SECOND_ENGINE_START = "Second engine start"
ROCKET_FAIRING_SEPARATION = "Fairing separation"
ROCKET_SECOND_ENGINE_CUT_OFF = "Second engine cut-off"
PAYLOAD_SEPARATION = "Payload separation"
FIRST_STAGE_FLIP_MANEUVER = "Flip maneuver"
FIRST_STAGE_ENTRY_BURN = "Entry burn"
FIRST_STAGE_GUIDANCE = "Guidance"
FIRST_STAGE_LANDING_BURN = "Landing burn"
FIRST_STAGE_LANDING_LEGS_DEPLOYED = "Landing legs deployed"
FIRST_STAGE_LANDING = "Landing" 

destroy = False
stop = False


# rocket = SimpleXMLRPCServer(('localhost', 8888), logRequests=True, allow_none=True)

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
                        group_id='rocket-simulation-group',
                        value_deserializer=lambda x: loads(x.decode('utf-8')))
    
consumer.subscribe(['launcherTopic'])
print("ok")
def printAndSendMessages(TOPIC, MESSAGE, rocketNameToSend, siteNameToSend):
    print(MESSAGE)
    data = { 'action' : MESSAGE,
        'siteName' : siteNameToSend,
        'rocketName' : rocketNameToSend
    }
    producer.send(TOPIC, value=data)
    time.sleep(1)




for msg in consumer:
    message = msg.value
    print(message['action'])
    
    if(msg.topic == 'launcherTopic' and message['action'] == LAUNCH):
        siteName = message['siteName']
        rocketName = message['rocketName']
        # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
        currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
        someRocketStates = json.loads(dumps(db.rocketsStates.find_one({"rocketName": rocketName, "siteName": siteName, "satelliteName": currentPayload.json()["satellite"]})))
        statesArray = someRocketStates["rocketStatesHe"]
        #s = ServerProxy(PAYLOAD_STATES_BASE_URL)

        # Envoi des étapes de lancement de la fusée 
        printAndSendMessages(ROCKET_TOPIC, LAUNCH, siteName, rocketName)

        printAndSendMessages(LAUNCHER_TOPIC, ROCKET_PREPARATION, siteName, rocketName)

        printAndSendMessages(LAUNCHER_TOPIC, ROCKET_ON_INTERNAL_POWER, siteName, rocketName)

        printAndSendMessages(LAUNCHER_TOPIC, ROCKET_STARTUP, siteName, rocketName)

        printAndSendMessages(LAUNCHER_TOPIC, ROCKET_MAIN_ENGINE_START, siteName, rocketName)

        printAndSendMessages(LAUNCHER_TOPIC, ROCKET_LIFTOFF, siteName, rocketName)

        length = len(statesArray)
        for index in range(0, length):
            if destroy is True:
                print("Rocket destruction!!!!")
                data = { 'action' : ROCKET_DESTRUCTION,
                    'siteName' : siteName,
                    'rocketName' : rocketName,
                }
                producer.send(ROCKET_TOPIC, value=data)
                producer.send(LAUNCHER_TOPIC, value=data)
                stop = True
                break
            
            if index == int(length / 2):
                printAndSendMessages(LAUNCHER_TOPIC, ROCKET_MAX_Q, siteName, rocketName)
                print("Max Q making us reduce the speed to 9")
                response = requests.put(
                    "{}//rocket/setRocketSpeed/{}/{}".format(BASE_URL_ROCKET_INVENTORY, rocketName, 9))
                time.sleep(5)
                print("Returning to initial speed")
                result = requests.put(
                    "{}//rocket/setRocketSpeed/{}/{}".format(BASE_URL_ROCKET_INVENTORY, rocketName, 10))
                printAndSendMessages(LAUNCHER_TOPIC, ROCKET_MAIN_ENGIE_CUT_OFF, siteName, rocketName)


            if index == int(3 * length / 4):
                print("Stage Seperation")
                printAndSendMessages(LAUNCHER_TOPIC, STAGE_SEPARATION, siteName, rocketName)
                printAndSendMessages(LAUNCHER_TOPIC, ROCKET_SECOND_ENGINE_CUT_OFF, siteName, rocketName)
                printAndSendMessages(LAUNCHER_TOPIC, PAYLOAD_SEPARATION, siteName, rocketName)
                

            time.sleep(4)

            data = { 'action' : RUNNING,
                    'siteName' : siteName,
                    'rocketName' : rocketName, 
                    'state': str(statesArray[index])}
            producer.send('rocketTopic', value=data)

            if index == length - 1:
                data = { 'action' : "end",
                    'siteName' : siteName,
                    'rocketName' : rocketName,
                    'state': str(statesArray[index])}
            producer.send('rocketTopic', value=data)
            

        if stop is False:
            print("Rocket at the end of the launch")
        # MAJ du statut de la mission (PAST)
        myobj = {
            "rocketName": rocketName
        }
        requests.post("{}/payload/setPastMissionValue".format(DELIVERY_STATES_BASE_URL), data=myobj)

    if(msg.topic == LAUNCHER_TOPIC and message['action'] == ROCKET_DESTRUCTION):
        destroy = True