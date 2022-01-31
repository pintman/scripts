#!/bin/bash

API='https://bees.tbs1.de/readmysql.php'

# match iso date - e.g. 2022-01-31
pattern='[0-9]{4}-[01][0-9]-[0-3][0-9]'

echo "Zeitstempel Gewicht(kg) Temperatur(°C) Luftfeuchtigkeit(%) Luftdruck(hPa) Gehäusetemperatur(°C)"
lynx --dump $API | grep -E "$pattern" | head -n 1 | sed -e 's/   //'

