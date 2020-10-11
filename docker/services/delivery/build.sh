#!/bin/bash

echo "Building delivery_service docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../services/delivery/. resources
docker build -t djotiham/delivery_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
