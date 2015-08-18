#!/bin/bash

# scan a network for clients and try to read a discover.txt file provided on
# port 80. An easy version for this would be a python server running with
#
# python -m SimpleHTTPServer 80
#
#
# Author: Marco Bakera
#

# Check for arguments.
if [[ -z $1 ]]; then
  SCRIPT=$(basename $0)
  echo To invoke the script give a network as first parameter.
  echo $SCRIPT NETWORK
  echo e.g. $SCRIPT 192.168.10.0/24
  
  exit
fi

NETWORK=$1

# You can change the port that is serving the discovery.txt file
# default: 80
PORT=80

# Use nmap to discover hosts on the network that are pingable.
IPS=$(nmap -sP $NETWORK | grep "scan report"| cut -d '(' -f 2 | cut -d ')' -f 1)

for ip in $IPS; 
do 
  RES=$(curl -s $ip:$PORT/discover.txt | head -1)
  echo $ip: $RES
done

