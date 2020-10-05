from xmlrpc.client import ServerProxy

s = ServerProxy('http://0.0.0.0:9000')

if __name__ == "__main__":
    while True:
        command = input().split(' ')
        if (command[0] == "quit"):
            print("Bye")
            break
        if(command[0] == "startpoll"):
            print(s.getResponsesPoll(command[1],command[2]))
        if(command[0] == "decide"):
            print("The rocket {} at {} : {}".format(command[3],command[2],command[1]))