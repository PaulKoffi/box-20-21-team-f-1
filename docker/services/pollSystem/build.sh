#!/bin/bash

echo "Building pollsystem_rpc docker image"
mkdir resources
cp ../../../requirements.txt resources
cp ../../../services/pollSystem/pollsystem.py resources
docker build -t djotiham/pollsystem_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
