#!/bin/bash

echo "Building supplier_rest_service docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../services/supplier/. resources
docker build -t djotiham/supplier_rest_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
