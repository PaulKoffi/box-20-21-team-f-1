#!/bin/bash

echo "Building rocket_rpc docker image"
mkdir resources
cp ../../../requirements.txt resources
cp ../../../rpc/rocket/secondStage.py resources
docker build -t djotiham/rocket_second_stage_rpc .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
