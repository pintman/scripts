#!/bin/bash

# This script is used to determine and announce the currently active ip
# addres. This can be used for a headless driven raspberry pi. I can be
# installed in a crontab with 'crontab -e' and the entry
#
# or, to send it every minute:
#
# * * * * * /path/to/script.sh
#
# This will send the IP adresse every minute. Change the default settings to
# your needs in the section below.
#
# Author: Marco Bakera
#

# The interface that should be used to fetch the IP address.
# default: eth0
INTERFACE=eth0

#
# Settings for the IRC-Server
#

# Use this IRC-Server to send a message about the IP address.
# default: irc.freenode.net
IRC_SERVER=irc.freenode.net

# Username that will send  a message sent to an IRC channel.
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

# check if we have an IP address.
test -z "$IP" && exit 1

# -s adjusts the speaking speed 
# the soundfile will be created first and played afterwards.
echo $IP | espeak -s 120 -w /tmp/ip.wav
aplay /tmp/ip.wav

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