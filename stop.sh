#!/bin/bash

## >>>>> Stop all servers : different CLIs, rpc and services
cd docker
docker-compose down

echo "Remove all images"

docker rmi djotiham/gywnne_cli
docker rmi djotiham/richardcli
docker rmi djotiham/torycli
docker rmi djotiham/eloncli

docker rmi djotiham/gwynne_dashboard
docker rmi djotiham/jeff_dashboard
docker rmi djotiham/victor_dashboard
docker rmi djotiham/mary_dashboard

docker rmi djotiham/payload_telemetry_server
docker rmi djotiham/rocket_telemetry_server

docker rmi djotiham/rocket_first_stage_rpc
docker rmi djotiham/djotiham/rocket_second_stage_rpc
docker rmi djotiham/payload_rpc

docker rmi djotiham/pollcreator_rpc
docker rmi djotiham/pollsystem_service

docker rmi djotiham/rocket_inventory_service
docker rmi djotiham/weather_service

docker rmi djotiham/delivery_service
docker rmi djotiham/launcher_service
docker rmi djotiham/satellite_service
docker rmi djotiham/event_registration_service
docker rmi djotiham/rocket_inventory_rest_service
docker rmi djotiham/supplier_rest_service

docker rmi djotiham/event_collector

docker rmi djotiham/trigger_anomaly_service
docker rmi djotiham/supplier_rpc_service

docker rmi djotiham/unit_tests
docker rmi djotiham/tests

docker rmi wurstmeister/kafka
docker rmi wurstmeister/zookeeper

echo "Done"
# echo "Done"
# read -n 1 -s -r -p "Press any key to continue"