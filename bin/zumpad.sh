#!/bin/bash
#
# show the content of a given zum pad

if [[ -z $1 ]] ;
then
	echo "Gib den Name des Pads an"
	exit 1
fi

curl https://zumpad.zum.de/p/$1/export/txt

