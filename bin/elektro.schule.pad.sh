#!/bin/bash
#
# show the content of a given pad at elektro.schule

if [[ -z $1 ]] ;
then
	echo "Das Skript zeigt den Inhalt eines Etherpads an."
	echo "Gib den Name des Pads an"
	exit 1
fi

curl https://elektro.schule/pad/p/$1/export/txt

