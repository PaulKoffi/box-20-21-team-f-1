from xmlrpc.server import SimpleXMLRPCServer
import requests

pollServer = SimpleXMLRPCServer(('0.0.0.0', 9000), logRequests=True, allow_none=True)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
ELON_URL = "http://localhost:8000/"
TORY_URL = "http://localhost:3000/"


def getResponsesPoll(siteName, rocketName):
    print(siteName + "\n" + rocketName)
    responseElon = requests.get("{}rocket/{}".format(ELON_URL, rocketName))
    responseTory = requests.get("{}siteByName/{}".format(TORY_URL, siteName))
    wind = responseTory.json()[0]['wind']
    rocketStatus = responseElon.json()['status']
    if (wind < 10) and rocketStatus == "it's risky":
        return {
            "elonResponse": "NOGO",
            "toryResponse": "GO",
            "richardResponse": "NOGO",
            "siteName": siteName,
            "rocketName": rocketName
        }
    elif (wind > 10) and rocketStatus == "ready to go":
        return {
            "elonResponse": "GO",
            "toryResponse": "NOGO",
            "richardResponse": "NOGO",
            "siteName": siteName,
            "rocketName": rocketName
        }

    elif (wind < 10) and rocketStatus == "ready to go":
        responseLaunching = requests.put(
            "{}/rocketsStates/launching/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName, 1))
        return {
            "elonResponse": "GO",
            "toryResponse": "GO",
            "richardResponse": "GO",
            "siteName": siteName,
            "rocketName": rocketName
        }
    else:
        return {
            "elonResponse": "NOGO",
            "toryResponse": "NOGO",
            "richardResponse": "NOGO",
            "siteName": siteName,
            "rocketName": rocketName
        }


pollServer.register_function(getResponsesPoll)
if __name__ == '__main__':
    try:
        print('Poll serving ....')
        pollServer.serve_forever()
    except KeyboardInterrupt:
        print('Poll exiting !!!')
