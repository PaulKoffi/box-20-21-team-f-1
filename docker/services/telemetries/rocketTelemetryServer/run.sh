#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:9490 to container:9490
docker run --name rocket_telemetry_server --rm -d -p 9490:9490 djotiham/rocket_telemetry_server

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
