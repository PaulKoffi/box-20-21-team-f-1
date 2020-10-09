import socket
import requests

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

BASE_URL = "http://localhost:7000"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and listen

serverSocket.bind(("127.0.0.1", 9292))

serverSocket.listen()

tab = []
val = False
rocketName = ""
arrayLength = 0
round = 0

# Accept connections
while (True):

    (clientConnected, clientAddress) = serverSocket.accept()

    if val is False:
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))
        tab.append(clientConnected)
        val = True
    else:
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))
        dataFromClient = clientConnected.recv(1024)

        print(dataFromClient.decode())

        # send data to jeff
        tab[0].send(bytes(dataFromClient.decode(), "utf-8"))

        if round == 0:
            rocketName = dataFromClient.decode()
        if round == 1:
            arrayLength = int(dataFromClient.decode())
        round += 1
        if round == 7:
            print("LAST DATA")
            response = requests.get("{}/payload/payloadByRocketName/{}".format(BASE_URL, rocketName))
            print(response.json())
            # print(response.json()["finalPosition"])
            if int(response.json()["finalPosition"]) == int(dataFromClient.decode()):
                myobj = {
                    "rocketName": rocketName
                }
                x = requests.post("{}/payload/setStatus".format(BASE_URL), data=myobj)
                if x.status_code != 403:
                    print("--------------< Satellite mis en Orbite avec succès >------------------")
            else:
                print("ECHEC DE LA MISSION")
            round = 0
