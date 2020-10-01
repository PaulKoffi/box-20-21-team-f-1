#!/bin/bash

echo "Building torycli docker image"
mkdir resources
cp ../../../CLIs/tory/toryCLI.py resources
docker build -t djotiham/torycli .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')