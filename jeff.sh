#!/bin/bash

## launch tests with docker

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker attach jeff_dashboard
else
		winpty docker attach jeff_dashboard
fi

echo "Done"
read -n 1 -s -r -p "Press any key to continue"