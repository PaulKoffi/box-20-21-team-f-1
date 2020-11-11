#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:8888 to container:8888
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name rocket_first_stage_rpc --rm -it -v `pwd`:/host-rocket_first_stage_rpc djotiham/rocket_first_stage_rpc
else
		winpty docker run --name rocket_first_stage_rpc --rm -it -v `pwd`:/host-rocket_first_stage_rpc djotiham/rocket_first_stage_rpc
fi

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
