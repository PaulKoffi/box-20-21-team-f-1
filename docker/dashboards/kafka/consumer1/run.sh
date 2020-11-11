#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - execute commands (-it)
# echo $OSTYPE
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name consumer1 --rm -it -v `pwd`:/host-consumer1 djotiham/consumer1
else
		winpty docker run --name consumer1 --rm -it -v `pwd`:/host-consumer1 djotiham/consumer1
fi

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
