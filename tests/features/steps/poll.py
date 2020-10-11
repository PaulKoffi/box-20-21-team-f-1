# from behave import *
# from xmlrpc.client import ServerProxy

# s = ServerProxy('http://localhost:9000')

# @given('we want to launch a rocket at a site')
# def step_impl(context):
#     pass

# @when('Richard starts the poll of the rocket {rocketName} at {siteName}')
# def step_impl(context,rocketName,siteName):
#     pass

# @then("He will receive Elon's response on {rocketName} is : {elonResponse:w}\\nTory's response on {siteName} is : {toryResponse:w} and the final response is : {richardResponse}")
# def step_impl(context,rocketName,elonResponse,siteName,toryResponse,richardResponse):
#     response = s.getResponsesPoll(siteName,rocketName)

#     assert context.failed is False
#     assert elonResponse == response["elonResponse"]
#     assert toryResponse == response["toryResponse"]
#     assert richardResponse == response["richardResponse"]


# @when('Richard starts the poll for rocket {rocketName} at {siteName}')
# def step_impl(context,rocketName,siteName):
#     pass

# @then("He will receive Elon's response on {rocketName} is : {elonResponse:w}\\nTory's response on {siteName} is : {toryResponse:w} so the final response is : {richardResponse}")
# def step_impl(context,rocketName,elonResponse,siteName,toryResponse,richardResponse):
#     response = s.getResponsesPoll(siteName,rocketName)

#     # assert context.failed is False
#     assert elonResponse == response["elonResponse"]
#     assert toryResponse == response["toryResponse"]
#     assert richardResponse == response["richardResponse"]