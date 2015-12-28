#!/bin/sh

MYSQL_PASS=wohnzimmer
HTTP_PORT=50080
MYSQL_PORT=53306

echo Starte Container.

docker run \
  --name=dvwa -d \
  -p $HTTP_PORT:80 -p $MYSQL_PORT:3306 \
  -e MYSQL_PASS=$MYSQL_PASS citizenstig/dvwa

echo Portweiterleitungen:
docker port dvwa

echo Zugangsdaten
echo "MySQL:        username=admin, password=$MYSQL_PASS"
echo "WebAnwendung: username=admin, password=password"
