#!/bin/bash

# Running the image as
#  - removing the container after exit,
#  - detached (-d),
#  - binding localhost:7000 to container:7000
docker run --name event_registration_service --rm -d -p 4000:4000 djotiham/event_registration_service
# to stop: docker stop ID
# to start a new shell in the container: docker exec -it ID bash
# to attach to the container: docker attach ID (^P ^Q to detach)
