#!/bin/bash

# This script is used to determine and play the currently active ip address
# onto the audio interface. It can be used for a headless driven raspberry pi
# and should be installed as crontab and executed every minute. Use 'crontab
# -e' and the following entry to accomplish this.
#
# * * * * * /path/to/script.sh
#
# Change the default settings to your needs in the section below.
#
# Author: Marco Bakera
#

# The interface that should be used to fetch the IP address.
# default: eth0
INTERFACE=eth0

# Determine the IP address.
IP=$(/sbin/ifconfig $INTERFACE | grep "inet " | cut -d : -f 2 | cut -d ' ' -f 1)

# check if we have an IP address and terminate otherwise.
test -z "$IP" && exit 1

# -s adjusts the speaking speed 
# the soundfile will be created first and played afterwards.
echo $IP | espeak -s 120 -w /tmp/ip.wav
aplay /tmp/ip.wav
