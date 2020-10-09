#!/bin/bash
# The goal of this file is to Load dependencies, compile if necessary, prepare the environment and starts the docker images
# To resume, prepare.sh = build.sh + launch.sh

cd docker/services
## >>>>> Building services <<<<<

## weather
cd weather
echo "Building weather service docker image"
./build.sh
cd ..
## rocket
cd rocketInventory
echo "Building rocketInventory service docker image"
./build.sh
cd ..

cd ../rpc
## >>>>> Building rpc <<<<<

## pollcreator
cd pollCreator
echo "Building pollCreator docker image"
./build.sh
cd ..

cd ../CLIs
## >>>>> Building CLIs <<<<<

## elon
cd elon
echo "Building elon docker image"
./build.sh
cd ..
## tory
cd tory
echo "Building tory docker image"
./build.sh
cd ..
## richard
cd richard
echo "Building richard docker image"
./build.sh
cd ..

cd ..
## >>>>> Running all servers
docker-compose up -d

# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"