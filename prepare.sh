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

cd eventCollector
# echo "Building rocketInventory service docker image"
./build.sh
cd ..

cd delivery
# echo "Building delivery service docker image"
./build.sh
cd ..

cd satellite
# echo "Building delivery service docker image"
./build.sh
cd ..

cd rocketInventory_REST
./build.sh
cd ..

cd eventRegistration
# echo "Building delivery service docker image"
./build.sh
cd ..

cd pollSystem
./build.sh
cd ..

cd supplier_REST
./build.sh
cd .. 

cd triggerAnomaly
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
cd supplier 
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
cd ..

cd victor
./build.sh
cd ..

cd mary
./build.sh
cd ../..


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


echo "Done"

echo "Containers started ..."

cd logs/scripts
nohup ./pollSystem.sh &

nohup ./firstStage.sh &
nohup ./secondStage.sh &
nohup ./payload.sh &

nohup ./jeffDashboard.sh &
nohup ./gwynneDashboard.sh &
nohup ./maryDashboard.sh &
nohup ./victorDashboard.sh &

#nohup ./delivery.sh &

#nohup ./eventRegistration.sh &
nohup ./eventCollector.sh &


nohup ./payloadTelemetriesServer.sh &
nohup ./rocketTelemetriesServer.sh &
nohup ./pollCreator.sh &

nohup ./rockerInventory.sh &
#nohup ./rocketInventoryREST.sh &

#nohup ./satellite.sh &

nohup ./supplierRpc.sh &
#nohup ./supplierREST.sh &

nohup ./triggerAnomaly.sh &

nohup ./weather.sh &

docker exec tests ./run.sh
#nohup ./launcher.sh &
#read -n 1 -s -r -p "Press any key to continue"
