#!/bin/bash

CONTAINER=debian_test
SSHPORT=5022

docker run --name=$CONTAINER -i -d -p $SSHPORT:22 debian:latest bash

# update system and install ssh server
docker exec $CONTAINER apt-get update
docker exec $CONTAINER apt-get install -y openssh-server
docker exec $CONTAINER service ssh start

# Adding users
for i in 1 2 3 4 5 6 7 8 9; do
docker exec $CONTAINER groupadd testuser$i
docker exec $CONTAINER useradd -m -g testuser$i -s /bin/bash testuser$i
docker exec $CONTAINER bash -c "echo testuser$i:123456 | chpasswd"
done

echo SSH server running on port $SSHPORT
echo press enter to stop and remove container
read

echo shutting down and removing container $CONTAINER
docker stop $CONTAINER
docker rm $CONTAINER
