#!/bin/bash

URL=https://warwick.ac.uk/fac/sci/dcs/research/ias/software/sherlock/sherlock.jar

TGT=$(dirname "$0")

if [ ! -f $TGT/sherlock.jar ]; then
	echo "download to $TGT"
	cd $TGT && wget $URL
fi

java -jar $TGT/sherlock.jar
