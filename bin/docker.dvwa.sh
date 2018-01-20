#!/bin/sh
#

HTTP_PORT=1080

echo Starte Container.

docker run \
  --name=dvwa -d \
  -p $HTTP_PORT:80 \
  vulnerables/web-dvwa

echo Portweiterleitungen:
docker port dvwa

