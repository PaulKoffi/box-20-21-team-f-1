#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:9000 to container:9000
docker run --name pollcreator_rpc --rm -d -p 9000:9000 djotiham/pollcreator_rpc

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
