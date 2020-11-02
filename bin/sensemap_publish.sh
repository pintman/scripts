#!/bin/bash

if [ -z $senseBoxId ]; then
    echo env var senseBoxId missing
    exit 1
fi

if [ -z $sensorId ]; then
    echo env var sensorId missing
    exit 1
fi

if [ -z $1 ]; then
    echo no data for sending 
    exit 1
fi

echo sending value $1 to sensemap endpoint
api=https://api.opensensemap.org/boxes/$senseBoxId/$sensorId

if [ -z $authToken ]; then
    echo env var authToken missing - sending without
    curlopts="-H Content-Type:application/json"
else
    curlopts="-H Content-Type:application/json -H Authorization:$authToken"
fi

curl -s -d "{\"value\":$1}" $curlopts $api
