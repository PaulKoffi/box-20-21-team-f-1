from xmlrpc.server import SimpleXMLRPCServer
import requests
import json
import time
import socket
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps, loads

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 9090        # Port to listen on (non-privileged ports are > 1023)

pollServer = SimpleXMLRPCServer(('localhost',8888 ),logRequests=True, allow_none=True)

client = pymongo.MongoClient("mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin') 

def sendRocketStates(siteName, rocketName):
    someRocketStates = json.loads(dumps(db.rocketsStates.find_one( {"rocketName": "Paris"})))
    statesArray = someRocketStates["rocketStatesHe"]
    length = len(statesArray)
    for index in range (0, length-1):
        time.sleep(5)
        # Create a client socket
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Connect to the server
        clientSocket.connect((HOST,PORT))
        # Send data to server
        data = str(statesArray[index])
        clientSocket.send(data.encode())

    
    return "{}".format()

pollServer.register_function(sendRocketStates)

if __name__ == '__main__':
    try:
        print('Poll serving ....')
        pollServer.serve_forever()

    except KeyboardInterrupt:
        print('Poll exiting !!!')