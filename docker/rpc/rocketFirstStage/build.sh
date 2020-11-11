#!/bin/bash

echo "Building rocket_first_stage_rpc docker image"
mkdir resources
cp ../../../requirements.txt resources
cp ../../../rpc/rocket/firstStage.py resources
cp ../../../rpc/rocket/constants.py resources
docker build -t djotiham/rocket_first_stage_rpc .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
