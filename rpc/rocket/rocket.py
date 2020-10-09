from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9090  # Port to listen on (non-privileged ports are > 1023)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
rocket = SimpleXMLRPCServer(('localhost', 8888), logRequests=True, allow_none=True)

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


def sendStates(siteName, rocketName):
    print("Hello")
    someRocketStates = json.loads(dumps(db.rocketsStates.find_one({"rocketName": rocketName, "siteName": siteName})))
    statesArray = someRocketStates["rocketStatesHe"]
    print(statesArray)

    # Envoi du code de la Rocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    data = rocketName
    clientSocket.send(data.encode())

    while True:
        responseLaunching = requests.get("{}/rocketsStates/launching/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName))
        if responseLaunching.text == "True":
            print("Launching started")   
            length = len(statesArray)
            for index in range(0, length):
                responseDestruction = requests.get("{}/rocketsStates/destruction/{}/{}".format(ROCKETS_STATES_BASE_URL, siteName, rocketName))
                if responseDestruction.text == "True":
                    print("Rocket destruction!!!!")
                    break
                time.sleep(5)
                # Create a client socket
                clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Connect to the server
                clientSocket.connect((HOST, PORT))
                # Send data to server
                data = str(statesArray[index])
                clientSocket.send(data.encode())
            print("Rocket at the end of the launch")
            break

    return ""


rocket.register_function(sendStates)

if __name__ == '__main__':
    try:
        print('rocket serving ....')
        rocket.serve_forever()

    except KeyboardInterrupt:
        print('rocket exiting !!!')
