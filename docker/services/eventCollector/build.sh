#!/bin/bash

echo "Building pollcreator_rpc docker image"
mkdir resources
cp ../../../requirements.txt resources
cp ../../../services/eventCollector/eventCollector.py resources
docker build -t djotiham/event_collector .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
