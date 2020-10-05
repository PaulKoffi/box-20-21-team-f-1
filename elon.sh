#!/bin/bash

## launch eloncli with docker

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker attach eloncli
else
		winpty docker attach eloncli
fi

echo "Done"
read -n 1 -s -r -p "Press any key to continue"