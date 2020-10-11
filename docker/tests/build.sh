#!/bin/bash

echo "Building rocket_service docker image"
mkdir resources
cp ../../requirements.txt resources
cp -R ../../tests/features/. resources
docker build -t djotiham/tests .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
