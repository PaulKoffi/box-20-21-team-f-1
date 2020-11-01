#!/bin/bash

echo "Building eloncli docker image"
mkdir resources
cp ../../../CLIs/elon/eloncli.py resources
docker build -t djotiham/eloncli .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
