#!/bin/bash
#
# TODO Wird sudo benötigt? Falls ja, könnten für bestimmte Programme 
# (python, python3, pydoc, ...) Rechte in sudoers eingeraeum werden.
#

# Username für den neuen User
USER=exam$RANDOM

# Prüfen, ob das Skript mit Rootrechten ausgefuehrt wird.
f [[ $(whoami) != "root" ]];
then
	echo "Bitte mit root-Rechten ausführen - z.B. mit sudo.";
	exit 1;
fi

# Prüfen, ob der zu erstellende User bereits vorhanden ist.
if grep $USER /etc/passwd ; 
then
	echo "User existiert bereits!";
	exit 1;
fi

# Der neue User wird mit einem neuen Passwort angelegt.
echo "User $USER wird angelegt."
useradd -m $USER
echo "Passwort für den neuen User $USER eingeben (und merken)"
passwd $USER

# Verzeichnisse in /home/ nicht mehr zugaenglich machen.
chmod go-x /home/*

