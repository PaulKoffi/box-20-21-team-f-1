#!/bin/bash

echo "Building delivery_service docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../services/rocketInventory_REST/. resources
docker build -t djotiham/rocket_inventory_rest_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
