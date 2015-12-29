#!/bin/bash

# scan a network for clients and and print out the arp cache afterwards to get
# the MAC adresses of the clients.
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

# Use nmap to discover hosts on the network that are pingable.
nmap -sP $NETWORK > /dev/null
# print out the arp cache
arp | grep :

