#!/bin/bash

API='https://bees.tbs1.de/readmysql.php'

today=$(date +%Y-%m-%d)

echo "Zeitstempel Gewicht(kg) Temperatur(°C) Luftfeuchtigkeit(%) Luftdruck(hPa) Gehäusetemperatur(°C)"
lynx --dump $API | grep $today | head -n 1 | sed -e 's/   //'

