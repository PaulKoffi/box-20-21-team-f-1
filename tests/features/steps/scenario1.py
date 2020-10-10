from behave import *
from xmlrpc.client import ServerProxy
import time
import requests

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"
responsePoll = ""


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
