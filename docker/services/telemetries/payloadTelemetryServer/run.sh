#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:9292 to container:9292
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name rocket_telemetry_server --rm -it -v `pwd`:/host-rocket_telemetry_server djotiham/rocket_telemetry_server
else
		winpty docker run --name rocket_telemetry_server --rm -it -v `pwd`:/host-rocket_telemetry_server djotiham/rocket_telemetry_server
fi
# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
