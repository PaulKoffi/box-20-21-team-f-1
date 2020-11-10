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

consumer3 = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollsystemTest4-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['pollelonresponsetopic'])
consumer1.subscribe(
    ['polltoryresponsetopic'])
consumer2.subscribe(
    ['launcherTopic'])
consumer3.subscribe(
    ['testTopic'])

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')
db.payloads.delete_one({"satellite": "CATACOMBE"})


@given(
    'un client Francis et son adresse mail francis@gmail.com et une nouvelle fusée SPACE001 enrégistré dans notre BD')
def step_impl(context):
    pass


@given('un satellite au nom de CATACOMBE')
def step_impl(context):
    pass


@given('la position finale de ce satellite est 20')
def step_impl(context):
    pass


@when('Gwynne enregistre cette nouvelle mission')
def step_impl(context):
    myquery = {"satelliteName": "CATACOMBE"}
    newvalues = {"$set": {"telemetriesData": [0, 0, 0, 0, 5, 6, 7, 8, 10, 10, 10, 9, 8, 7, 6, 5, 4, 1, 0]}}
    db.anomalyRocketLaunchTelemetriesDataMocked.update_one(myquery, newvalues)
    myobj = {
        "customerName": "Francis",
        "customerMail": "francis@gmail.com",
        "finalPosition": 20,
        "x": 5,
        "y": 5,
        "satellite": "CATACOMBE"
    }
    requests.post(DELIVERY_STATES_BASE_URL, json=myobj)


@then("On voit qu'une fusée disponible a été affecté à la mission")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CATACOMBE"))
    assert response.json()['satellite'] == "CATACOMBE"
    assert response.json()['rocketName'] == "SPACE001"


@then("la fusée disponible est SPACE001")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CATACOMBE"))
    assert response.json()['rocketName'] == "SPACE001"


@given('Toulouse un site où la pression du vent actuellement est au dessus de notre seuil de sécurité')
def step_impl(context):
    pass


@given('la fusée SPACE001 qui est affecté à la mise en orbite du satellite CATACOMBE')
def step_impl(context):
    pass


@when("richard décide de démarrer le poll pour l'envoi de la fusée")
def step_impl(context):
    r = s.getResponsesPoll("Toulouse", "SPACE001")


@then("On voit que Elon donne son GO car la fusée est en état")
def step_impl(context):
    for msg in consumer:
        message = msg.value
        topic_retrieve = msg.topic
        if (topic_retrieve == 'pollelonresponsetopic'):
            assert message['response']['status'] == "ready to go"
            break


@then("On voit que la réponse de Tory est NOGO car Toulouse est une zone à risque")
def step_impl(context):
    for msg in consumer1:
        message = msg.value
        topic_retrieve = msg.topic
        if topic_retrieve == 'polltoryresponsetopic' and message['response']['name'] == 'Toulouse':
            responseTory = message['response']
            print(responseTory)
            assert responseTory['wind'] >= 10
            break


@then("et que la réponse de Richard est donc NOGO")
def step_impl(context):
    pass


@given('Paris un site où la pression du vent actuellement est normale')
def step_impl(context):
    pass


# consumer.poll()
# consumer.seek_to_end()
# consumer1.poll()
# consumer1.seek_to_end()
# consumer2.poll()
# consumer2.seek_to_end()


@when("richard décide de démarrer son poll")
def step_impl(context):
    r = s.getResponsesPoll("Paris", "SPACE001")


# consumer3 = KafkaConsumer(
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='latest',
#     enable_auto_commit=False,
#     group_id='pollsystemTest3-group',
#     value_deserializer=lambda x: loads(x.decode('utf-8')))
#
# consumer4 = KafkaConsumer(
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='latest',
#     enable_auto_commit=False,
#     group_id='pollsystemTest4-group',
#     value_deserializer=lambda x: loads(x.decode('utf-8')))
#
# consumer5 = KafkaConsumer(
#     bootstrap_servers=['localhost:9092'],
#     auto_offset_reset='latest',
#     enable_auto_commit=False,
#     group_id='pollsystemTest5-group',
#     value_deserializer=lambda x: loads(x.decode('utf-8')))


@then("On voit que Elon donne son GO car la fusée est dans un bon état")
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


@then("On voit que la réponse de Tory est GO car les conditions atmosphériques de Paris sont aussi bonnes")
def step_impl(context):
    i = 0

    for msg in consumer1:
        i = i + 1
        # print(i)
        # if i == 2:
        message = msg.value
        topic_retrieve = msg.topic
        # print("2")
        print(message['response'])
        if topic_retrieve == 'polltoryresponsetopic' and message['response']['name'] == 'Paris':
            responseTory = message['response']
            #     print(responseTory)
            assert responseTory['wind'] < 10
        break


@then("et que la réponse de Richard est alors GO")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "launch":
            break


@then("Rocket Preparation")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Rocket preparation":
            break


@then("Rocket on internal power")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Rocket on internal power":
            break


@then("Startup")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Startup":
            break


@then("Main engine start")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Main engine start":
            break


@then("Liftoff/Launch")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Liftoff":
            break


@then("Max Q")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Max Q":
            break


@then("Main engine cut-off")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Main engine cut-off":
            break


@then("Stage separation")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Second stage separation":
            break


@then("Second engine start")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Second engine start":
            break


@then("Fairing separation")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Fairing separation":
            break


@then("Second engine cut-off")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Second engine cut-off":
            break


@then("Payload separation/deploy")
def step_impl(context):
    for msg in consumer2:
        message = msg.value
        if msg.topic == 'launcherTopic' and message['action'] == "Payload separation":
            break


# def verifyIsMessageIsAlreadyInTopic(msg,message):
#     if msg.topic == 'launcherTopic' and message['action'] == "Flip maneuver":
#     elif msg.topic == 'launcherTopic' and message['action'] == "Entry burn":
#     elif msg.topic == 'launcherTopic' and message['action'] == "Guidance":
#     elif msg.topic == 'launcherTopic' and message['action'] == "Entry burn":
#     elif msg.topic == 'launcherTopic' and message['action'] == "Entry burn":
#     elif msg.topic == 'launcherTopic' and message['action'] == "Entry burn":
#
#
# Flip_maneuver = False
# Entry_burn = False
# Guidance = False
# Landing_burn = False
# Landing_legs_deployed = False
# Landing = False

@then("Flip maneuver")
def step_impl(context):
    for msg in consumer3:
        message = msg.value
        print(message['action'])
        if msg.topic == 'testTopic' and message['action'] == "Flip maneuver":
            break


@then("Entry burn")
def step_impl(context):
    for msg in consumer3:
        message = msg.value
        if msg.topic == 'testTopic' and message['action'] == "Entry burn":
            break


@then("Guidance")
def step_impl(context):
    for msg in consumer3:
        message = msg.value
        if msg.topic == 'testTopic' and message['action'] == "Guidance":
            break


@then("Landing burn")
def step_impl(context):
    for msg in consumer3:
        message = msg.value
        if msg.topic == 'testTopic' and message['action'] == "Landing burn":
            break


@then("Landing legs deployed")
def step_impl(context):
    for msg in consumer3:
        message = msg.value
        if msg.topic == 'testTopic' and message['action'] == "Landing legs deployed":
            break


@then("Landing")
def step_impl(context):
    for msg in consumer3:
        message = msg.value
        if msg.topic == 'testTopic' and message['action'] == "Landing":
            break


@when("Quand on verifie la disponibilité de la fusée attribué à la mission")
def step_impl(context):
    context.rocket = requests.get("{}/rocketN/{}".format(BASE_URL_ROCKET_INVENTORY, "SPACE001"))


@then("elle est bien à True")
def step_impl(context):
    assert context.rocket.json()["available"] is True


@when("Quand on verifie le statut Past de la mission")
def step_impl(context):
    context.payload = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CATACOMBE"))


@then("il est aussi à True")
def step_impl(context):
    assert context.payload.json()["past"] is True


@when("Quand on verifie le succès de la mission")
def step_impl(context):
    time.sleep(20)
    context.payload = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CATACOMBE"))


@then("il est bien à True")
def step_impl(context):
    assert context.payload.json()["success"] is True
    # myquery = {"satellite": "CATACOMBE"}
    # newvalues = {"$set": {"past": False, "success": False}}
    # db.payloads.update_one(myquery, newvalues)
    db.payloads.delete_one({"satellite": "CATACOMBE"})
