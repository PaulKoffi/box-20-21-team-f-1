#!/bin/bash
# The goal of this file is to Load dependencies, compile if necessary, prepare the environment and starts the docker images
# To resume, prepare.sh = build.sh + 5nch.sh

cd docker/services
## >>>>> Building services <<<<<

## weather
cd weather
# echo "Building weather service docker image"
./build.sh
cd ..
## launcher
cd launcher
# echo "Building launcher service docker image"
./build.sh
cd ..
## rocket
cd rocketInventory
# echo "Building rocketInventory service docker image"
./build.sh
cd ..
cd delivery
# echo "Building delivery service docker image"
./build.sh
cd ..

cd pollSystem
./build.sh
cd ..

cd telemetries
## >>>>> Building servers socket <<<<<

cd payloadTelemetryServer
# echo "Building delivery service docker image"
./build.sh
cd ..
cd rocketTelemetryServer
# echo "Building delivery service docker image"
./build.sh
cd ..

cd ../../rpc
## >>>>> Building rpc <<<<<

## pollcreator
cd pollCreator
# echo "Building pollCreator docker image"
./build.sh

cd ..
cd rocketFirstStage
# echo "Building rocket firstStage docker image"
./build.sh

cd ..
cd rocketSecondStage
# echo "Building rocket secondStage docker image"
./build.sh

cd ..
cd payload
# echo "Building payload docker image"
./build.sh
cd ..

cd ../dashboards
## >>>>> Building dashboards <<<<<

## jeff dashboard
cd jeff
# echo "Building elon docker image"
./build.sh
cd ..
## gwynne dashboard
cd gwynne
# echo "Building tory docker image"
./build.sh
cd ../..

# cd kafka
# cd consumer1
# ./build.sh
# cd ..
# cd producer
# ./build.sh

# cd ../..

cd CLIs
## >>>>> Building CLIs <<<<<

## elon
cd elon
# echo "Building elon docker image"
./build.sh
cd ..
## tory
cd tory
# echo "Building tory docker image"
./build.sh
cd ..
## richard
cd richard
# echo "Building richard docker image"
./build.sh
cd ..
## gwynne
cd gwynne
# echo "Building richard docker image"
./build.sh
cd ..

cd ../tests
## >>>>> Building Tests <<<<<

# echo "Building tests docker image"
./build.sh
cd ..
cd unitTests
./build.sh
cd ..

## >>>>> Running all servers
docker-compose up -d

cd ..
## Displaying dashboards
#echo "Displaying dashboards"
#if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
#        sudo apt install gnome-terminal
#        gnome-terminal -- ./jeff.sh
#        gnome-terminal -- ./gwynne.sh
#else
#		echo "Go to docker desktop to see appropriate logs."
#fi


echo "Done"
docker exec -it -d pollcreator_rpc python pollcreator.py
docker exec -it -d rocket_inventory_service python run.py
docker exec -it -d weather_service python run.py
docker exec -it -d rocket_telemetry_server python rocketTelemetriesServer.py
docker exec -it -d payload_telemetry_server python payloadTelemetriesServer.py
docker exec -it -d jeff_dashboard python jeffdashboard.py
docker exec -it -d gwynne_dashboard python gwinedashboard.py
docker exec -it -d pollsystem_service python pollsystem.py
#read -n 1 -s -r -p "Press any key to continue"