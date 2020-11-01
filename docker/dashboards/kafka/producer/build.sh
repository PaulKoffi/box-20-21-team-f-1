#!/bin/bash

echo "Building producer docker image"
mkdir resources
cp ../../../../requirements.txt resources
cp -R ../../../../dashboard/kafka/producer.py resources
docker build -t djotiham/producer .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
