#!/bin/bash

echo "Building supplier rpc service docker image"
mkdir resources
cp ../../../requirements.txt resources
cp -R ../../../rpc/supplier/fuelSupplier.py resources
docker build -t djotiham/supplier_rpc_service .
rm -R resources
# to remove old images
# docker rmi $(docker images -qa -f 'dangling=true')
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"
