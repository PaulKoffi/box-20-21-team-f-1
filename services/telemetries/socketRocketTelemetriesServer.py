import socket
import requests
import pymongo

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

BASE_URL = "http://localhost:8000"
client = pymongo.MongoClient(
    "mongodb+srv://flo:Azerty123@cluster0.ibhol.mongodb.net/blueOrigin?retryWrites=true&w=majority")
db = client.get_database('blueOrigin')
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and listen

serverSocket.bind(("127.0.0.1", 9490))

serverSocket.listen()

tab = []
telemetriesData = []
val = False
rocketName = ""
arrayLength = 0
round = 0


def saveTelemetriesData():
    values = {
        "machine": rocketName,
        "type": "ROCKET",
        "projectionTelemetriesData": [int(i) for i in telemetriesData[2:]]
    }
    db.projectionTelemetriesData.insert_one(values)
    return "";


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

        # send data to jeff
        tab[0].send(bytes(dataFromClient.decode(), "utf-8"))

        if round == 0:
            rocketName = dataFromClient.decode()
        # if round == 1:
        #     arrayLength = int(dataFromClient.decode())
        round += 1
        telemetriesData.append(dataFromClient.decode())

        # if destruction
        if dataFromClient.decode() == "STOP":
            round = 0
            telemetriesData = []

        if round == 21:
            # Enregistrement des données telemetriques
            saveTelemetriesData()

            print("LAST DATA")
            if 0 == int(dataFromClient.decode()):
                print("--------------< La rocket a atteri avec succès  >------------------")
                # Rendre la rocket à nouveau disponible
                response = requests.post("{}/rocket/setStatus/{}".format(BASE_URL, rocketName))
                if response.status_code == 403:
                    print(" ERREUR !")
                else:
                    print(" La rocket {} est de nouveau disponible pour une mission !".format(rocketName))
            else:
                print("La rocket est endommagée !!")
            round = 0
            telemetriesData = []

