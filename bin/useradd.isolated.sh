#!/bin/bash

USER=exam

if [[ grep $USER /etc/pass ]];
	echo "User existiert bereits!";
	exit 1;
fi

sudo useradd -m $USER
echo "Passwort für den neuen User eingeben (und merken)"
sudo passwd $USER


sudo chmod go-x /home/*

