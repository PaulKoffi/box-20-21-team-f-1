#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:2650 to container:2650
docker run --name supplier_rest_service --rm -d -p 2650:2650 djotiham/supplier_rest_service
# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
