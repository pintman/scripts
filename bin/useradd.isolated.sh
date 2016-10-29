#!/bin/bash
#
# Das Skript erstellt einen neuen User und entfernt den Zugriff auf 
# die Home-Verzeichnisse anderer User. Es muss mit sudo oder als root
# ausgeführt werden.
#
# TODO Wird sudo benötigt? Falls ja, könnten für bestimmte Programme 
# (python, python3, pydoc, ...) Rechte in sudoers eingeräumt werden.
#
# TODO Mit ansible lässt sich dieses Skript sicher besser realisieren.

# Username für den neuen User
USER=exam$RANDOM

# Prüfen, ob das Skript mit Rootrechten ausgefuehrt wird.
if [[ $(whoami) != "root" ]];
then
	echo "Bitte mit root-Rechten ausführen - z.B. mit sudo.";
	exit 1;
fi

# Prüfen, ob der zu erstellende User bereits vorhanden ist.
if grep $USER /etc/passwd; 
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

