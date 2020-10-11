import socket
import requests
import pymongo

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

BASE_URL = "http://localhost:7000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and listen

serverSocket.bind(("127.0.0.1", 9292))

serverSocket.listen()

tab = []
val = False
telemetriesData = []
satelliteName = ""
arrayLength = 0
round = 0


def saveTelemetriesData():
    values = {
        "machine": satelliteName,
        "type": "PAYLOAD",
        "projectionTelemetriesData": [int(i) for i in telemetriesData[2:]]
    }
    db.projectionTelemetriesData.insert_one(values)
    return ""


# Accept connections
while (True):

    (clientConnected, clientAddress) = serverSocket.accept()
    print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

    if val is False:
        tab.append(clientConnected)
        val = True
    else:
        dataFromClient = clientConnected.recv(1024)
        print(dataFromClient.decode())

        # send data to Gwynne
        tab[0].send(bytes(dataFromClient.decode(), "utf-8"))

        if round == 0:
            satelliteName = dataFromClient.decode()
        # if round == 1:
        #     arrayLength = int(dataFromClient.decode())
        telemetriesData.append(dataFromClient.decode())
        round += 1

        # if destruction
        if dataFromClient.decode() == "STOP":
            round = 0
            telemetriesData = []
            response = requests.get("{}/payload/payloadBySatelliteName/{}".format(BASE_URL, satelliteName))
            myobj = {
                "rocketName": str(response.json()["rocketName"])
            }
            x = requests.post("{}/payload/setStatus".format(BASE_URL), data=myobj)

        if round == 9:
            # Enregistrement des données telemetriques
            saveTelemetriesData()

            print("LAST DATA")
            response = requests.get("{}/payload/payloadBySatelliteName/{}".format(BASE_URL, satelliteName))
            print(response.json())
            # print(response.json()["finalPosition"])
            if int(response.json()["finalPosition"]) == int(dataFromClient.decode()):
                myobj = {
                    "rocketName": str(response.json()["rocketName"])
                }
                x = requests.post("{}/payload/setStatus".format(BASE_URL), data=myobj)
                if x.status_code != 403:
                    print("--------------< Satellite mis en Orbite avec succès >------------------")
            else:
                print("ECHEC DE LA MISSION")
            round = 0
            telemetriesData = []
