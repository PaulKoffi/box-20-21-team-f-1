#!/bin/bash

echo "Building satellite_service docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../services/satellite/. resources
docker build -t djotiham/satellite_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
