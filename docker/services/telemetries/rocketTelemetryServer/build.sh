#!/bin/bash

echo "Building socket rocket telemetry server docker image"
mkdir resources
cp ../../../../requirements.txt resources
cp -R ../../../../services/telemetries/socketRocketTelemetriesServer.py resources
docker build -t djotiham/rocket_telemetry_server .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
