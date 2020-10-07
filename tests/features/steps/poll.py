from behave import *
from xmlrpc.client import ServerProxy

s = ServerProxy('http://localhost:9000')

@given('we want to launch a rocket at a site')
def step_impl(context):
    pass

@when('Richard start the poll of the rocket {rocketName:w} at {siteName:w}')
def step_impl(context,rocketName,siteName):
    response = s.getResponsesPoll(siteName,rocketName)
    assert rocketName == "cotonou"
    assert siteName == "Paris"

@then("He will receive Elon's response on cotonou is : {elonResponse:w}\\nTory's response on Paris is : {toryResponse:w}")
def step_impl(context,elonResponse,toryResponse):
    # ELON_URL = "http://0.0.0.0:8000/"
    # TORY_URL = "http://0.0.0.0:3000/"
    # responseElon = requests.get("{}rocket/{}".format(ELON_URL,"cotonou"))
    # responseTory = requests.get("{}siteByName/{}".format(TORY_URL,"Paris"))
    response = s.getResponsesPoll("Paris","cotonou")
    response_splitted = response.split(' ')
    # print(reponse)
    assert context.failed is False
    assert elonResponse+"\nTory's" == response_splitted[6]
    assert toryResponse == response_splitted[12]
    # print(response)