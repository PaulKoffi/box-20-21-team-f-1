#!/bin/bash

echo "Building rocket_service docker image"
mkdir resources
cp ../../../services/rocket/requirements.txt resources
cp -R ../../../services/rocket/src/ resources
docker build -t djotiham/rocket_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
