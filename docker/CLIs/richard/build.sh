#!/bin/bash

echo "Building richardcli docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../CLIs/richard/richardcli.py resources
docker build -t djotiham/richardcli .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
