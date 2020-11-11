#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:8282 to container:8282
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name payload_rpc --rm -it -v `pwd`:/host-payload_rpc djotiham/payload_rpc
else
		winpty docker run --name payload_rpc --rm -it -v `pwd`:/host-payload_rpc djotiham/payload_rpc
fi


# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
