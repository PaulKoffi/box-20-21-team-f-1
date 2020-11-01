#!/bin/bash


# Running the image as
#  - removing the container after exit,
#  - execute commands (-it)
# echo $OSTYPE
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name unit_tests --rm -it -v `pwd`:/host-unit_tests djotiham/unit_tests
else
		winpty docker run --name unit_tests --rm -it -v `pwd`:/host-unit_tests djotiham/unit_tests
fi

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
