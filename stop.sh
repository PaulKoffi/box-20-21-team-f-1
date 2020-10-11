#!/bin/bash

## >>>>> Stop all servers : different CLIs, rpc and services
cd docker
docker-compose down

# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"