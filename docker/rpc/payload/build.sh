#!/bin/bash

echo "Building payload_rpc docker image"
mkdir resources
cp ../../../requirements.txt resources
cp ../../../rpc/payload/payload.py resources
docker build -t djotiham/payload_rpc .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
