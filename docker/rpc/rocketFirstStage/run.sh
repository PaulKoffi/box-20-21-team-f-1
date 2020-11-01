#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:8888 to container:8888
docker run --name rocket_first_stage_rpc --rm -d -p 8888:8888 djotiham/rocket_first_stage_rpc

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
