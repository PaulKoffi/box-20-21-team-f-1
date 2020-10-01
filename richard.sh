#!/bin/bash

## launch richardcli with docker

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker attach richardcli
else
		winpty docker attach richardcli
fi
