from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads
from xmlrpc.client import ServerProxy

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9490  # Port to listen on (non-privileged ports are > 1023)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
PAYLOAD_STATES_BASE_URL = "http://localhost:8282"
BASE_URL_ROCKET_INVENTORY = "http://localhost:8000"
DELIVERY_STATES_BASE_URL = "http://localhost:7000"

rocket = SimpleXMLRPCServer(('localhost', 8888), logRequests=True, allow_none=True)

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


def sendStates(siteName, rocketName):
    # Recuperation de la mission actuelle de la Rocket (PAST == FALSE)
    currentPayload = requests.get("{}/payload/payloadByRocketName/{}".format(DELIVERY_STATES_BASE_URL, rocketName))
    someRocketStates = json.loads(
        dumps(db.rocketsStates.find_one(
            {"rocketName": rocketName, "siteName": siteName, "satelliteName": currentPayload.json()["satellite"]})))
    # print(someRocketStates)
    statesArray = someRocketStates["rocketStatesHe"]
    s = ServerProxy(PAYLOAD_STATES_BASE_URL)

    # Envoi du nom de la rocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    data = rocketName
    clientSocket.send(data.encode())

    # Envoi de la taille du tableau
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    data = str(len(statesArray))
    clientSocket.send(data.encode())

    while True:
        responseLaunching = requests.get(
            "{}/rocketsStates/launching/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName))
        if responseLaunching.text == "True":
            print("Launching started")
            length = len(statesArray)
            stop = False
            for index in range(0, length):
                responseDestruction = requests.get(
                    "{}/rocketsStates/destruction/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName))

                if responseDestruction.text == "True":
                    print("Rocket destruction!!!!")
                    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    clientSocket.connect((HOST, PORT))
                    data = "STOP"
                    stop = True
                    clientSocket.send(data.encode())
                    break
                if index == int(length / 2):
                    print("Rocket secondStep!!!!")
                    requests.put(
                        "{}/rocketsStates/secondStep/{}/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName, 1))
                    s.sendPayloadStates(siteName, rocketName)

                if index == int(3 * length / 4):
                    print("Max Q making us reduce the speed to 9")
                    response = requests.put(
                        "{}//rocket/setRocketSpeed/{}/{}".format(BASE_URL_ROCKET_INVENTORY, rocketName, 9))
                    time.sleep(2)
                    print("Returning to initial speed")
                    result = requests.put(
                        "{}//rocket/setRocketSpeed/{}/{}".format(BASE_URL_ROCKET_INVENTORY, rocketName, response))

                time.sleep(2)

                # Create a client socket
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Connect to the server
                clientSocket.connect((HOST, PORT))
                # Send data to server
                data = str(statesArray[index])
                clientSocket.send(data.encode())
            if stop is False:
                print("Rocket at the end of the launch")
            # MAJ du statut de la mission (PAST)
            myobj = {
                "rocketName": rocketName
            }
            requests.post("{}/payload/setPastMissionValue".format(DELIVERY_STATES_BASE_URL), data=myobj)

            break

    return ""


rocket.register_function(sendStates)

if __name__ == '__main__':
    try:
        print('rocket serving ....')
        rocket.serve_forever()

    except KeyboardInterrupt:
        print('rocket exiting !!!')