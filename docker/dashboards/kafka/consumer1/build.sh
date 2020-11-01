#!/bin/bash

echo "Building consumer1 docker image"
mkdir resources
cp ../../../../requirements.txt resources
cp -R ../../../../dashboard/kafka/consumer1.py resources
docker build -t djotiham/consumer1 .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
