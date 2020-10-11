#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - execute commands (-it)
# echo $OSTYPE
if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker run --name jeff_dashboard --rm -it -v `pwd`:/host-jeffdashboard djotiham/jeff_dashboard
else
		winpty docker run --name jeff_dashboard --rm -it -v `pwd`:/host-jeffdashboard djotiham/jeff_dashboard
fi

# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
