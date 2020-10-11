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


def elonOrder():
    s1.sendStates("Paris", "VEGA-4000")


@given('un client ayant comme Nom Francis et adresse mail francis@gmail.com')
def step_impl(context):
    pass


@given('un satellite au nom de CORSAIRE')
def step_impl(context):
    pass


@given('la position finale de ce satellite ayant comme valeur 12')
def step_impl(context):
    pass


@when('Gwynne enregistre cette nouvelle mission')
def step_impl(context):
    myobj = {
        "customerName": "Francis",
        "customerMail": "francis@gmail.com",
        "finalPosition": 12,
        "x": 5,
        "y": 5,
        "satellite": "CORSAIRE"
    }
    requests.post(DELIVERY_STATES_BASE_URL, data=myobj)


@then("On voit qu'une fusée disponible a été affecté à la mission et qu'elle a été bien crée")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CORSAIRE"))
    assert response.json()['satellite'] == "CORSAIRE"
    assert response.json()['rocketName'] != ""


@then("la fusée disponible est VEGA-4000")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CORSAIRE"))
    assert response.json()['rocketName'] == "VEGA-4000"


@given('Toulouse un site où la pression du vent actuellement est au dessus de notre seuil de sécurité')
def step_impl(context):
    pass


@given('la fusée VEGA-4000 qui est affecté à la mise en orbite du satellite CORSAIRE')
def step_impl(context):
    pass


@when("richard décide de démarrer le poll pour l'envoi de la fusée")
def step_impl(context):
    context.responsePoll = s.getResponsesPoll("Toulouse", "VEGA-4000")


@then("On voit que Elon donne son GO car la fusée est en état")
def step_impl(context):
    assert context.responsePoll['elonResponse'] == "GO"


@then("On voit que la réponse de Tory est NOGO car Toulouse est une zone à risque")
def step_impl(context):
    assert context.responsePoll['toryResponse'] == "NOGO"


@then("et que la réponse de Richard est donc NOGO")
def step_impl(context):
    assert context.responsePoll['richardResponse'] == "NOGO"


@given('Paris un site où la pression du vent actuellement est au dessus de notre seuil de sécurité')
def step_impl(context):
    pass


@when("richard décide de démarrer le poll")
def step_impl(context):
    context.responsePoll = s.getResponsesPoll("Paris", "VEGA-4000")


@then("On voit que Elon donne son GO car la fusée est en état de décoller")
def step_impl(context):
    assert context.responsePoll['elonResponse'] == "GO"


@then("On voit que la réponse de Tory est GO car les conditions atmosphériques de Paris sont bonnes")
def step_impl(context):
    assert context.responsePoll['toryResponse'] == "GO"


@then("et que la réponse de Richard est donc GO")
def step_impl(context):
    assert context.responsePoll['richardResponse'] == "GO"


@given('le GO de Richard')
def step_impl(context):
    pass


@when("on consulte le statut du lancement de la fusée")
def step_impl(context):
    context.rocket = requests.get("{}/rocket/{}".format(BASE_URL_ROCKET_INVENTORY, "VEGA-4000"))
    context.rocketLaunched = requests.get(
        "{}/rocketsStates/launching/{}/{}".format(ROCKETS_STATES_BASE_URL, "Paris", "VEGA-4000"))


@then("on voit qu'il est bien à True")
def step_impl(context):
    assert context.rocketLaunched.text == "True"


@then("la fusée est toujours indisponible pour une autre mission pour le moment")
def step_impl(context):
    assert context.rocket.json()["available"] is False


@given('le GO de Richard accordé à Elon')
def step_impl(context):
    pass


@when("Elon donne l'ordre de lancement de la fusée")
def step_impl(context):
    os.chdir('steps/utils')
    subprocess.Popen(["python.exe", "elonOrder.py"])


@when("on consulte le statut success du Payload auquel est affectée la fusée VEGA-4000")
def step_impl(context):
    context.payload = requests.get("{}/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, "VEGA-4000"))


@then("on voit qu'il est à False et que l'attribut Past qui indique que la mission est terminée est aussi à False")
def step_impl(context):
    assert context.payload.json()["success"] is False
    assert context.payload.json()["past"] is False


@then("le statut pour passer au detachement de la fusée est à False")
def step_impl(context):
    context.rocketSecondStep = requests.get(
        "{}/rocketsStates/secondStep/{}/{}".format(ROCKETS_STATES_BASE_URL, "Paris", "VEGA-4000"))
    assert context.rocketSecondStep.text == "False"


@when("On consulte la vitesse de la fusée actuellement")
def step_impl(context):
    context.rocketSpeed = requests.get("{}/rocket/{}".format(BASE_URL_ROCKET_INVENTORY, "VEGA-4000"))


@then("Sa vitesse est 10")
def step_impl(context):
    assert context.rocketSpeed.json()["speed"] == 10


@when("Après 27 secondes on consulte le statut qui indique le detachement en 2 de la fusées")
def step_impl(context):
    time.sleep(25)
    context.rocketSecondStep = requests.get(
        "{}/rocketsStates/secondStep/{}/{}".format(ROCKETS_STATES_BASE_URL, "Paris", "VEGA-4000"))


@then("il est maintenant à True et donc le satellite sera bientôt en Orbite")
def step_impl(context):
    assert context.rocketSecondStep.text == "True"


@when("On consulte maintenant les détails du Payload après 20s")
def step_impl(context):
    time.sleep(20)
    context.payload = requests.get("{}/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, "VEGA-4000"))


@then(
    "On voit que Success est à True et Past toujours à False : L'orbite est en place mais la fusée n'a pas encore atteri sur terre")
def step_impl(context):
    assert context.payload.json()["success"] is True
    assert context.payload.json()["past"] is False


@when("On consulte la vitesse actuelle de la fusée après 10s")
def step_impl(context):
    time.sleep(10)
    context.rocketSpeed = requests.get("{}/rocket/{}".format(BASE_URL_ROCKET_INVENTORY, "VEGA-4000"))


@then("Elle est à 9 et donc la fusée est au MaxQ")
def step_impl(context):
    assert context.rocketSpeed.json()["speed"] == 9


@when("On consulte après 20s à nouveau le statut Past et la disponibilité de la rocket VEGA-4000")
def step_impl(context):
    time.sleep(20)
    context.payload = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL, "CORSAIRE"))
    context.rocket = requests.get("{}/rocket/{}".format(BASE_URL_ROCKET_INVENTORY, "VEGA-4000"))


@then("La fusée est à nouveau disponible et Past à True indique que la mission est terminée")
def step_impl(context):
    assert context.payload.json()["past"] is True
    assert context.rocket.json()["available"] is True

    # MAJ de la BD pour le prochain scénario
    myquery = {"rocketName": "VEGA-4000"}
    newvalues = {"$set": {"launch": False, "secondStep": False}}
    db.rocketActions.update_one(myquery, newvalues)
    db.payloads.delete_one({"satellite": "CORSAIRE"})
    db.rocketinventories.delete_one({"rocketName": "VEGA-4000"})
    db.rocketinventories.insert_one({
        "rocketName": "VEGA-4000",
        "available": True,
        "fuel": "5000",
        "status": "ready to go",
        "speed": 10
    })
