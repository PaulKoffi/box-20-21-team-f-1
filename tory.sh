#!/bin/bash

## launch torycli with docker

if [[ "$OSTYPE" == "linux-gnu"* || "$OSTYPE" == "darwin"* ]]; then
        docker attach torycli
else
		winpty docker attach torycli
fi
