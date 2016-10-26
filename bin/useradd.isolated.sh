#!/bin/bash

USER=exam$RANDOM

if [[ $(whoami) != "root" ]];
then
	echo "Bitte mit root-Rechten ausführen - z.B. mit sudo.";
	exit 1;
fi

if grep $USER /etc/passwd ; 
then
	echo "User existiert bereits!";
	exit 1;
fi

echo "User $USER wird angelegt."
useradd -m $USER
echo "Passwort für den neuen User $USER eingeben (und merken)"
passwd $USER


chmod go-x /home/*

