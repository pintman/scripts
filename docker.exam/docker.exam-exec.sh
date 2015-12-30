#!/bin/bash
#
# Execute a given command in every running container.
#

# Check for number of arguments
if [[ -z $* ]]; then
  echo Give me a command to be executed in each container.
  exit 1
fi

# fetch ids of all running containers
#
# --format not present in older versions of docker
#IDS=$(docker ps --format "{{.ID}}")
IDS=$(docker ps | cut -d ' ' -f 1 | tail -n +2)

for i in $IDS; 
do 
    echo Container $(docker inspect -f "{{.Name}}" $i) $i
    docker exec $i $* 
done
