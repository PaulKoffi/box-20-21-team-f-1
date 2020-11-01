#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:8888 to container:8888
docker run --name rocketFirstStage_rpc --rm -d -p 8888:8888 djotiham/rocketFirstStage_rpc

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
