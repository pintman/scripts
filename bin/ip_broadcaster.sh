#!/bin/bash

# This script is used to determine and announce the currently active ip
# address. It can be used for a headless driven raspberry pi and should be
# installed as crontab and executed every minute. Use 'crontab -e' and the
# following entry to accomplish this.
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

#
# Settings for the IRC-Server
#

# Use this IRC-Server to send a message that contains the IP address.
# default: irc.freenode.net
IRC_SERVER=irc.freenode.net

# Username that will send a message to an IRC channel. The hostname is a good
# choice for this.  
# default: ip_broadcaster
USER=ip_broadcaster

# The port of the IRC server.
# default: 6667
IRC_PORT=6667

# The name of the channel the message should be send to.
# default: #ip_broadcaster
CHANNEL=#ip_broadcaster

# Determine the IP address.
IP=$(/sbin/ifconfig $INTERFACE | grep "inet " | cut -d : -f 2 | cut -d ' ' -f 1)

# A message that will be sent to the channel. Use ':' to start the message
# part.  
# default: ":My local IP is $IP"
MSG=":My local IP is $IP"

#
# Configuration END
#

# check if we have an IP address and terminate otherwise.
if [[ -z "$IP" ]]
then
	echo Konnte keine IP-Adresse ermitteln.
	exit 1
fi


# send the ip to the irc server via nc
#
(
echo NICK $USER
sleep 2
echo USER $USER 8 * : $USER
sleep 2
echo "JOIN $CHANNEL"
sleep 2
echo "PRIVMSG $CHANNEL $MSG."
sleep 2
echo QUIT
) | nc $IRC_SERVER $IRC_PORT
