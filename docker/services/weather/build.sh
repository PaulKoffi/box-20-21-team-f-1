#!/bin/bash

echo "Building weather_service docker image"
mkdir resources
cp -R ../../../services/weather/. resources
docker build -t djotiham/weather_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
