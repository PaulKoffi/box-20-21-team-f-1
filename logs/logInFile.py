import docker

client = docker.from_env()
containerList = client.containers.list()

Dict = {"djotiham/rocket_inventory_rest_service": "rocketInventoryRestServiceLogs.log",
        "djotiham/event_registration_service": "eventRegistrationServiceLogs.log",
        "djotiham/satellite_service": "satelliteServiceLogs.log",
        "djotiham/supplier_rest_service": "supplierRestServiceLogs.log",
        "djotiham/delivery_service": "deliveryServiceLogs.log",
        "djotiham/launcher_service": "launcherServiceLogs.log"}

# print(l)
for e in containerList:
    # print(e.id)
    container = client.containers.get(e.id)
    if container.attrs['Config']['Image'] in Dict:
        print("LOG DE :  " + container.attrs['Config']['Image'])
        f = open(Dict.get(container.attrs['Config']['Image']), "w")
        f.write(str(container.logs(), 'utf-8').strip() + "\n")
        f.close()
        print("FIN LOG DE :  " + container.attrs['Config']['Image'])

        # break
