from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9292  # Port to listen on (non-privileged ports are > 1023)
ROCKETS_STATES_BASE_URL = "http://localhost:5000"
BASE_URL = "http://localhost:7000/payload"
payload = SimpleXMLRPCServer(('localhost', 8282), logRequests=True, allow_none=True)

client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')


def sendPayloadStates(siteName, rocketName):
    someRocketStates = json.loads(dumps(db.rocketsStates.find_one({"rocketName": rocketName, "siteName": siteName})))
    # print(someRocketStates)
    paylaodStatesArray = someRocketStates["payloadStatesHe"]

    # Envoi du code de la Rocket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    data = requests.get("{}/payloadByRocketName/{}".format(BASE_URL, rocketName)).json()["satellite"]
    clientSocket.send(data.encode())

    # Envoi de la taille du tableau
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((HOST, PORT))
    data = str(len(paylaodStatesArray))
    clientSocket.send(data.encode())

    print("SecondState started: payload telemetry")
    l = len(paylaodStatesArray)
    for index in range(0, l):
        time.sleep(2)
        # Create a client socket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        clientSocket.connect((HOST, PORT))
        # Send data to server
        data = str(paylaodStatesArray[index])
        clientSocket.send(data.encode())
    print("Payload is stabilised")

    return ""

payload.register_function(sendPayloadStates)

if __name__ == '__main__':
    try:
        print('payload serving ....')
        payload.serve_forever()

    except KeyboardInterrupt:
        print('payload exiting !!!')
