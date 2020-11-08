#!/bin/bash

echo "Building mary_dashboard docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../dashboard/Mary/maryDashboard.py resources
docker build -t djotiham/mary_dashboard .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
