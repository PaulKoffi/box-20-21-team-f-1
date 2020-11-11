#!/bin/bash

## launch tests with docker

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker attach tests
else
		winpty docker attach tests
fi

echo "Done"
read -n 1 -s -r -p "Press any key to continue"