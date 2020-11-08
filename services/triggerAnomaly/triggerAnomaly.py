from kafka import KafkaConsumer
from json import loads, dumps
import requests
import pymongo
from kafka import KafkaProducer
from bson.json_util import dumps, loads
import json
from time import sleep

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='anomaly-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

consumer.subscribe(['rocketTopic', 'rocketSTopic', 'launcherTopic'])
previsions = []
i = 4
rocketName = ""
siteName = ""
ROCKETS_STATES_BASE_URL = "http://localhost:5000"

def getCurrentSatelliteName(rocketName):
    DELIVERY_STATES_BASE_URL = "http://localhost:7000"
    currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
    return currentPayload.json()["satellite"]

sleep(5)

for msg in consumer:
    message = msg.value
    topic_retrieve = msg.topic
    if msg.topic == 'launcherTopic' and message['action'] == "launch":
        i = 4
        rocketName = message['rocketName']
        siteName = message['siteName']
        satelliteName = getCurrentSatelliteName(message['rocketName'])
        previsions = json.loads(dumps(db.anomalyRocketLaunchTelemetriesDataMocked.find_one(
            {"rocketName": message['rocketName'], "satelliteName": satelliteName})))["telemetriesData"]
        print(previsions)
    if message['action'] == "running" and topic_retrieve == "rocketTopic":
        print(message['rocketName'] + " FIRST STAGE || " + " at position " + message['state'])
        i = i + 1
        print("PREVISION : " + str(previsions[i]))
        if int(previsions[i]) != int(message['state']):
            print("================ ANOMALY ====================")
            data = {'action': "DANGER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! : ANOMALY DETECTED IN FIRST STAGE, ++++ AUTOMATIC DESTRUCTION ACTIVED",
                    'siteName': siteName,
                    'rocketName': rocketName,
                    }
            # SET STOP LAUNCHING
            requests.put(
                "{}/rocketsStates/destruction/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName, 1))
            producer.send("anomalyTopic", value=data)
    elif message['action'] == "running" and topic_retrieve == "rocketSTopic":
        print(message['rocketName'] + " SECOND STAGE || " + " at position " + message['state'])

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))
