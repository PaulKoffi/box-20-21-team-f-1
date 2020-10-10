from behave import *
from xmlrpc.client import ServerProxy
import time
import requests

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
DELIVERY_STATES_BASE_URL = "http://localhost:7000/payload"

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
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL,"CORSAIRE"))
    assert response.json()['satellite'] == "CORSAIRE"
    assert response.json()['rocketName'] != ""

@then("la fusée disponible est VEGA-4000")
def step_impl(context):
    response = requests.get("{}/payloadBySatelliteName/{}".format(DELIVERY_STATES_BASE_URL,"CORSAIRE"))
    assert response.json()['rocketName'] == "VEGA-4000"
