import requests

BASE_URL = "http://localhost:7000/payload"

if __name__ == "__main__":
    while True:
        command = input().split(' ')
        if (command[0] == "quit"):
            print("Bye")
            break
        if (command[0] == "status"):
            response = requests.get("{}/payloadByRocketName/{}".format(BASE_URL, command[1]))
            if response.status_code == 403:
                print("PAYLOAD INCONNU !")
            else:
                print(response.json())
                print("STATUT : ", end="")
                print(response.json()["success"])
        if (command[0] == "addPayload"):
            print("-------------------------------------")
            print("")
            print("CUSTOMER NAME : ", end="")
            name = input()
            print("CUSTOMER MAIL : ", end="")
            mail = input()
            print("FINAL POSITION : ", end="")
            finalPosition = int(input())
            print("X : ", end="")
            x = int(input())
            print("Y : ", end="")
            y = int(input())
            print("SATELLITE NAME : ", end="")
            satellite = input()
            print("")
            print("-------------------------------------")

            myobj = {
                "customerName": name,
                "customerMail": mail,
                "finalPosition": finalPosition,
                "x": x,
                "y": y,
                "satellite": satellite
            }
            x = requests.post(BASE_URL, data=myobj)
            if x.status_code == 403:
                print("Aucune fusée disponible !")
            else:
                print("La fusée %s a été attribué à la mission !" % (x.json()["rocketName"]))
            print("")
