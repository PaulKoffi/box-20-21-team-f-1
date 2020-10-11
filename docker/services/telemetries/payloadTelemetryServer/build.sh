#!/bin/bash

echo "Building socket payload telemetry server docker image"
mkdir resources
cp ../../../../requirements.txt resources
cp -R ../../../../services/telemetries/socketPayloadTelemetriesServer.py resources
docker build -t djotiham/payload_telemetry_server .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
