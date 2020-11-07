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

consumer.subscribe(
    ['pollelonresponsetopic'])
consumer1.subscribe(
    ['polltoryresponsetopic'])
consumer2.subscribe(
    ['launcherTopic'])

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')

print("ici")


# def elonOrder():
#     s1.sendStates("Paris", "VEGA-4000")

@given('Paris un site sécurisé de lancement')
def step_impl(context):
    pass


@given('la fusée RIKIKI qui est affecté à la mise en orbite du satellite APOLLON')
def step_impl(context):
    pass


@when("richar décide de démarrer le poll pour l'envoi de la fusée")
def step_impl(context):
    # print("ici")
    # os.chdir('utils')
    # subprocess.Popen(["python", "elonOrder.py"])
    r = s.getResponsesPoll("Paris", "RIKIKI")

@then("On voit Elon donne son GO")
def step_impl(context):
    for msg in consumer:
        message = msg.value
        topic_retrieve = msg.topic
        if (topic_retrieve == 'pollelonresponsetopic'):
            assert message['response']['status'] == "ready to go"
            break

@then("On voit la réponse de Tory est GO")
def step_impl(context):
    for msg in consumer1:
        message = msg.value
        topic_retrieve = msg.topic
        if (topic_retrieve == 'polltoryresponsetopic'):
            responseTory = message['response']
            assert responseTory['wind'] < 10
            break


@then("et que Richard donne son GO")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        # print("LA")
        # print(message['action'])
        topic_retrieve = msg.topic
        if msg.topic == 'launcherTopic' and message['action'] == "launch":
            # print("Launch")
            break
    # pass

# for msg in consumer:
#     message = msg.value
#     topic_retrieve = msg.topic
#
#     if (topic_retrieve == 'pollelonresponsetopic'):
#         @then("On voit qu Elon donne son GO")
#         def step_impl(context):
#             assert message['response']['status'] == "ready to go"
#
#     if (topic_retrieve == 'polltoryresponsetopic'):
#         @then("On voit qu la réponse de Tory est GO")
#         def step_impl(context):
#             responseTory = message['response']
#             assert responseTory['wind'] < 10
#
#     if msg.topic == 'launcherTopic' and message['action'] == "launch":
#         @given('et que la répons de Richard est donc GO')
#         def step_impl(context):
#             pass
