#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:9292 to container:9292
docker run --name payload_telemetry_server --rm -d -p 9292:9292 djotiham/payload_telemetry_server

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
