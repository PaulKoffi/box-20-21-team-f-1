#!/bin/bash

echo "Building trigger anomaly docker image"
mkdir resources
cp ../../../requirements.txt resources
cp ../../../services/triggerAnomaly/triggerAnomaly.py resources
docker build -t djotiham/trigger_anomaly_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
