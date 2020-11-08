#!/bin/bash

echo "Building victor_dashboard docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../dashboard/victor/victorDashboard.py resources
docker build -t djotiham/victor_dashboard .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
