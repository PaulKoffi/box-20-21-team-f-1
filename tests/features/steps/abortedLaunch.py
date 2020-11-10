import os
from behave import *
from xmlrpc.client import ServerProxy
import time
import requests
from subprocess import Popen, PIPE
import subprocess
import pymongo
from kafka import KafkaConsumer
from kafka import KafkaProducer
from json import loads
from time import sleep
from json import dumps
import queue

sleep(10)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollsystemTest-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer1 = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollsystemTest1-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer2 = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollsystemTest2-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

# consumer3 = KafkaConsumer(
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='pollsystemTest4-group',
#     value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['pollelonresponsetopic'])
consumer1.subscribe(
    ['polltoryresponsetopic'])
consumer2.subscribe(
    ['launcherTopic'])
# consumer3.subscribe(
#     ['testTopic'])

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

db.payloads.delete_one({"satellite": "CATACOMBE"})


@given('Monaco un site où la pression du vent est actuellement normale')
def step_impl(context):
    pass


# consumer.poll()
# consumer.seek_to_end()
# consumer1.poll()
# consumer1.seek_to_end()
# consumer2.poll()
# consumer2.seek_to_end()


@when("richard démarre le poll")
def step_impl(context):
    myobj = {
        "customerName": "Francis",
        "customerMail": "francis@gmail.com",
        "finalPosition": 20,
        "x": 5,
        "y": 5,
        "satellite": "CATACOMBE"
    }
    requests.post(DELIVERY_STATES_BASE_URL, json=myobj)
    r = s.getResponsesPoll("Monaco", "SPACE001")


@then("Elon répond par GO")
def step_impl(context):
    i = 0
    for msg in consumer:
        i = i + 1
        print(i)
        # if i == 2:
        message = msg.value
        topic_retrieve = msg.topic
        # print("1")
        # print(message['response'])

        if (topic_retrieve == 'pollelonresponsetopic'):
            assert message['response']['status'] == "ready to go"
        break


@then("Tory répond par GO")
def step_impl(context):
    i = 0

    for msg in consumer1:
        i = i + 1
        print(i)
        # if i == 2:
        message = msg.value
        topic_retrieve = msg.topic
        # print("2")
        print(message['response'])
        if topic_retrieve == 'polltoryresponsetopic' and message['response']['name'] == 'Monaco':
            responseTory = message['response']
            print(responseTory)
            assert responseTory['wind'] < 10
            break


@then("Richard répond ensuite par GO")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "launch":
            break


@then("step : Rocket Preparation step")
def step_impl(context):
    requests.put(
        "{}/rocketsStates/destruction/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, "Monaco", "SPACE001", 1))
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Rocket preparation":
            break


@when("Richard lance l'ordre de destruction")
def step_impl(context):
    pass


@then("on voit que la mission est bien annulée")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "destroy":
            break
    myquery1 = {"satelliteName": "CATACOMBE", "siteName": "Monaco"}
    newvalues1 = {"$set": {"stopLaunching": False}}
    db.rocketActions.update_one(myquery1, newvalues1)
