#!/bin/bash

echo "Building gwyne cli docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../CLIs/gwynne/gwynnecli.py resources
docker build -t djotiham/gwynne_cli .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
