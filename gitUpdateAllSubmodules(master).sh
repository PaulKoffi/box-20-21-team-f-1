#!/bin/bash

## This script consists to fully update the project from root to all sub-modules
## simple update
echo "Updating root project"
git pull
## update all submodules
echo "Updating submodules"
git submodule update --init --recursive
## checkout every submodule to branch master
## weatherService
echo "Checkout weatherService on branch Master"
cd weatherService
git checkout master
git pull
cd ..
## rocketService
echo "Checkout rocketService on branch Master"
cd rocketService
git checkout master
git pull
cd ..
## pollCreator-rpc
echo "Checkout pollCreator-rpc on branch Master"
cd pollCreator-rpc
git checkout master
git pull
cd ..
## elonCLI
echo "Checkout elonCLI on branch Master"
cd elonCLI
git checkout master
git pull
cd ..
## richardCli
echo "Checkout richardCli on branch Master"
cd richardCli
git checkout master
git pull
cd ..
## toryCli
echo "Checkout toryCli on branch Master"
cd toryCli
git checkout master
git pull
cd ..

echo "Done"
read -n 1 -s -r -p "Press any key to continue"

