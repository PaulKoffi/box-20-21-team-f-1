#!/bin/bash

cd docker/services
## >>>>> Building services <<<<<

## weather
cd weather
./build.sh
cd ..
## rocket
cd rocket
./build.sh
cd ..

cd ../rpc
## >>>>> Building rpc <<<<<

## pollcreator
cd pollCreator
sh build.sh
cd ..

cd ../CLIs
## >>>>> Building CLIs <<<<<

## elon
cd elon
sh build.sh
cd ..
## tory
cd tory
sh build.sh
cd ..
## richard
cd richard
sh build.sh
cd ..

# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"