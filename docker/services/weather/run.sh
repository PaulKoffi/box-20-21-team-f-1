#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:8000 to container:8000
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name weather_service --rm -it -v `pwd`:/host-weather_service djotiham/weather_service
else
		winpty docker run --name weather_service --rm -it -v `pwd`:/host-weather_service djotiham/weather_service
fi
# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
