#!/bin/bash

. freifunk_common

if [ -z "$1" ]; then
    echo hide or show
    exit 1
fi

if [ "$1" = "hide" ]; then
    echo hiding location
    exec_ff uci set gluon-node-info.@location[0].share_location=0
fi
if [ "$1" = "show" ]; then
    echo showing location
    exec_ff uci set gluon-node-info.@location[0].share_location=1
fi

echo commiting changes
exec_ff uci commit gluon-node-info
exec_ff uci show gluon-node-info
