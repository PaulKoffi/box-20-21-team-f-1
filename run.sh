#!/bin/bash

## >>>>> Running all servers
cd docker
docker-compose up -d

echo "Done"
read -n 1 -s -r -p "Press any key to continue"