import socket

# Create a stream based socket(i.e, a TCP socket)

# operating on IPv4 addressing scheme

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind and listen

serverSocket.bind(("127.0.0.1", 9090))

serverSocket.listen()

tab = []
val = False

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
