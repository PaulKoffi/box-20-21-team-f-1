#!/bin/bash

## This script consists to fully update the project from root to all sub-modules
## simple update
echo "Updating root project"
git pull
## update all submodules
echo "Updating submodules"
git submodule update --init --recursive

echo "Done"
read -n 1 -s -r -p "Press any key to continue"

