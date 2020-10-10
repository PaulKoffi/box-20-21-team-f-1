from xmlrpc.server import SimpleXMLRPCServer
import requests

pollServer = SimpleXMLRPCServer(('0.0.0.0', 9000), logRequests=True, allow_none=True)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
ELON_URL = "http://localhost:8000/"
TORY_URL = "http://localhost:3000/"
DELIVERY_STATES_BASE_URL = "http://localhost:7000"


def getResponsesPoll(siteName, rocketName):
    responseElon = requests.get("{}rocket/{}".format(ELON_URL, rocketName))
    responseTory = requests.get("{}siteByName/{}".format(TORY_URL, siteName))
    wind = responseTory.json()[0]['wind']
    if (wind < 10):
        responseTory = "GO"
    else:
        responseTory = "NOGO"

    if (responseElon.json()['status'] == "it's risky"):
        responseElon = "NOGO"
    else:
        responseElon = "GO"
    if responseTory == "GO" and responseElon == "GO":
        responseLaunching = requests.put(
            "{}/rocketsStates/launching/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName, 1))
    return "Elon's response on {} is : {}\nTory's response on {} is : {}".format(rocketName, responseElon, siteName,
                                                                                 responseTory)


pollServer.register_function(getResponsesPoll)

if __name__ == '__main__':
    try:
        print('Poll serving ....')
        pollServer.serve_forever()
    except KeyboardInterrupt:
        print('Poll exiting !!!')
