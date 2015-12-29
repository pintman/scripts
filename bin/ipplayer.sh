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

# Speaking speed. The higher, the faster.
SPEED=100

# Determine the IP address.
# maybe this can accomplished easier with 'hostname -I'
IP=$(/sbin/ifconfig $INTERFACE | grep "inet " | cut -d : -f 2 | cut -d ' ' -f 1 | sed -e 's/\./ Punkt /g')

# check if we have an IP address and terminate otherwise.
test -z "$IP" && exit 1

# -s adjusts the speaking speed 
# the soundfile will be created first and played afterwards.
espeak -v de -s $SPEED -w /tmp/ip.wav "Meine IP Adresse ist $IP"
aplay /tmp/ip.wav
