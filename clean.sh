#!/bin/bash

## Removing all images
docker rmi djotiham/richardcli djotiham/torycli djotiham/eloncli djotiham/payload_telemetry_server djotiham/pollcreator_rpc djotiham/rocket_inventory_service djotiham/delivery_service djotiham/weather_service djotiham/launcher_service
## Removing old/dandling images
# docker rmi $(docker images -qa -f 'dangling=true')

# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"