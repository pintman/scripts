#!/usr/bin/bash

API='https://bees.tbs1.de/readmysql.php'

today=$(date --iso)

echo "Zeitstempel Gewicht(kg) Temperatur(°C) Luftfeuchtigkeit(%) Luftdruck(hPa) Gehäusetemperatur(°C)"
lynx --dump $API | grep $today | head -n 1

