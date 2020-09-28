#!/bin/bash

echo "Building the docker image"
mkdir resources
cp ../../../services/rocket/requirements.txt resources
cp -R ../../../services/rocket/src/ resources
docker build -t djotiham/rocket_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
echo "Done"
read -n 1 -s -r -p "Press any key to continue"
