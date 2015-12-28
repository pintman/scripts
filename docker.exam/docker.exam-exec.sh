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
IDS=$(docker ps --format "{{.ID}}")

for i in $IDS; 
do 
    echo Container $(docker inspect -f "{{.Name}}" $i) $i
    docker exec $i $* 
done
