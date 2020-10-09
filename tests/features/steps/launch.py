from behave import *
from xmlrpc.client import ServerProxy
import time
import requests

s = ServerProxy('http://localhost:9000')
s1 = ServerProxy('http://localhost:8888')
BASE_URL = "http://localhost:7000/payload"

@given('we will to launch a rocket at a site')
def step_impl(context):
    pass

@when('Richard starts the poll of the rocket {rocketName} at {siteName}')
def step_impl(context,rocketName,siteName):
    response = s.getResponsesPoll(siteName,rocketName)

@then('Elon sends the order to launch the rocket PGP-6000 at Paris')
def step_impl(context):
    response = s1.sendStates("Paris","PGP-6000")

@then("after 60 seconds , the satellite was successful delivered by PGP-6000")
def step_impl(context):
    time.sleep(60)
    response = requests.get("{}/payloadByRocketName/PGP-6000".format(BASE_URL))
    assert response.json()['success'] == True

    
