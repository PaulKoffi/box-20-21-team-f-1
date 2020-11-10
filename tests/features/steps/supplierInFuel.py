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

# sleep(10)

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

consumer = KafkaConsumer(
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='pollsystemTest8-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

consumer.subscribe(
    ['supplierTopic'])

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


@given('CORSAIRE un satellite dont le lancement a échoué')
def step_impl(context):
    pass


@when("Richard donne l'ordre de ravitaillement")
def step_impl(context):
    response = s.launchSupplier("ASTA", "CORSAIRE")


@then(
    "Il reçoit une erreur car le système après consultation s'est rendu compte que le satellite n'était pas en orbite")
def step_impl(context):
    for msg in consumer:
        message = msg.value
        if message['action'] == "notLaunchedYet":
            break


@given('APOLLON un satellite en Orbite')
def step_impl(context):
    pass


@when("Richard donne l'ordre de ravitaillement du satellite")
def step_impl(context):
    response = s.launchSupplier("ASTA", "APOLLON")


@then("La capsule se met en route")
def step_impl(context):
    for msg in consumer:
        message = msg.value
        if message['action'] == "launchSupplier":
            break


@then("La capsule envoit une notification dès qu'il commence le ravitaillement du satellite en Orbite")
def step_impl(context):
    for msg in consumer:
        message = msg.value
        if message['action'] == "supplied":
            break


@then("La capsule envoit de nouveau une notification quand il atterit sur terre")
def step_impl(context):
    for msg in consumer:
        message = msg.value
        if message['action'] == "back":
            break
