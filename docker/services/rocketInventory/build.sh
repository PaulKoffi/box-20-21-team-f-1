#!/bin/bash

echo "Building rocket_service docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../services/rocketInventory/. resources
docker build -t djotiham/rocket_inventory_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
