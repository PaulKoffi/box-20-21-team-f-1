import os
from behave import *
from xmlrpc.client import ServerProxy
import time
import requests
from subprocess import Popen, PIPE
import subprocess
import pymongo

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


@given(
    'un client Francis et son adresse mail francis@gmail.com et une nouvelle fusée SOUL-9000 enrégistré dans notre BD')
def step_impl(context):
    pass


@given('un satellite au nom de PERSEUS')
def step_impl(context):
    pass


@given('la position finale de ce satellite ayant est 12')
def step_impl(context):
    pass


@when('Gwynne enregistre cette nouvelle mission dans sa CLI')
def step_impl(context):
    # Ajout Rocket disponible SOUL-9000
    db.rocketinventories.insert_one({
        "rocketName": "SOUL-9000",
        "available": True,
        "fuel": "5000",
        "status": "ready to go",
        "speed": 10
    })

    myobj = {
        "customerName": "Francis",
        "customerMail": "francis@gmail.com",
        "finalPosition": 12,
        "x": 5,
        "y": 5,
        "satellite": "PERSEUS"
    }
    requests.post(DELIVERY_STATES_BASE_URL, data=myobj)


@then("On voit qu'une fusée disponible a été affecté à la mission")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "PERSEUS"))
    assert response.json()['satellite'] == "PERSEUS"
    assert response.json()['rocketName'] == "SOUL-9000"


@then("la fusée disponible est SOUL-9000")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "PERSEUS"))
    assert response.json()['rocketName'] == "SOUL-9000"


@given('Paris un site où la pression du vent actuellement est normale')
def step_impl(context):
    pass


@when("richard décide de démarrer son poll")
def step_impl(context):
    context.responsePoll = s.getResponsesPoll("Paris", "SOUL-9000")


@then("On voit que Elon donne son GO car la fusée est dans un bon état")
def step_impl(context):
    assert context.responsePoll['elonResponse'] == "GO"


@then("On voit que la réponse de Tory est GO car les conditions atmosphériques de Paris sont aussi bonnes")
def step_impl(context):
    assert context.responsePoll['toryResponse'] == "GO"


@then("et que la réponse de Richard est alors GO")
def step_impl(context):
    assert context.responsePoll['richardResponse'] == "GO"


@given('le GO accordé par Richard')
def step_impl(context):
    pass


@when("on consulte le statut du lancement de la fusée SOUL-9000")
def step_impl(context):
    context.rocket = requests.get("{}/rocket/{}".format(BASE_URL_ROCKET_INVENTORY, "SOUL-9000"))
    context.rocketLaunched = requests.get(
        "{}/rocketsStates/launching/{}/{}".format(ROCKETS_STATES_BASE_URL, "Paris", "SOUL-9000"))


@then("on voit qu'il est bien à True donc la fusée a ordre de décoller")
def step_impl(context):
    assert context.rocketLaunched.text == "True"


@then("la fusée est toujours indisponible pour une autre mission pour le moment quand on consulte son statut")
def step_impl(context):
    assert context.rocket.json()["available"] is False


@given('le GO de Richard accordé à Elon pour lancer la fusée')
def step_impl(context):
    pass


@when("Elon donne l'ordre de lancement de la fusée SOUL-9000")
def step_impl(context):
    os.chdir('utils')
    subprocess.Popen(["python", "elonOrder2.py"])


@when("on consulte le statut success du Payload auquel est affectée la fusée SOUL-9000")
def step_impl(context):
    context.payload = requests.get("{}/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, "SOUL-9000"))


@then(
    "on voit qu'il est à False et que l'attribut Past qui indique que la mission est terminée est toujours aussi à False")
def step_impl(context):
    # print("ici {}".format(context.payload.json()))
    assert context.payload.json()["success"] is False
    assert context.payload.json()["past"] is False


@when("Richard décide de stopper la mission")
def step_impl(context):
    requests.put("{}/rocketsStates/destruction/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, "Paris", "SOUL-9000", 1))


@then(
    "On voit que Success est à False et Past à True : La mission est passé et ça a été un échec")
def step_impl(context):
    time.sleep(10)
    context.payload = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "PERSEUS"))
    assert context.payload.json()["success"] is False
    assert context.payload.json()["past"] is True


@when("On consulte le statut disponible de la fusée SOUL-9000")
def step_impl(context):
    context.rocket = requests.get("{}/rocket/{}".format(BASE_URL_ROCKET_INVENTORY, "SOUL-9000"))


@then("Elle est indisponible car elle a été détruite")
def step_impl(context):
    assert context.rocket.json()["available"] is False

    # MAJ de la BD pour le prochain scénario
    myquery = {"rocketName": "SOUL-9000"}
    newvalues = {"$set": {"launch": False, "secondStep": False}}
    db.rocketActions.update_one(myquery, newvalues)
    db.payloads.delete_one({"satellite": "PERSEUS"})
    db.rocketinventories.delete_one({"rocketName": "SOUL-9000"})
