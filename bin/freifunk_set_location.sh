#!/bin/bash

. freifunk_common

if [ -z "$1" ]; then
    echo "westenfelder oder ostring"
    exit 1
fi

if [ "$1" = "westenfelder" ]; then
    echo "using coordinates for westenfelder str."
    lat=51.464715978
    lon=7.149983346
fi

if [ "$1" = "ostring" ]; then
    echo "using coordinates for ostring"
    lat=51.480530986
    lon=7.225586772
fi

if [ -z "$lat" ]; then
    echo "westefenfelder oder ostring"
    exit 1
fi

exec_ff uci set gluon-node-info.@location[0].latitude=$lat
exec_ff uci set gluon-node-info.@location[0].longitude=$lon
echo "commiting changes"
exec_ff uci commit gluon-node-info
exec_ff "uci show | grep gluon-node-info"
