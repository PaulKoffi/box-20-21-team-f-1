#!/bin/bash

echo "Building pollcreator_rpc docker image"
mkdir resources
cp ../../../rpc/pollCreator/pollcreator.py resources
docker build -t djotiham/pollcreator_rpc .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
