#!/bin/sh

# Starte services
/etc/init.d/ssh start
/etc/init.d/apache2 start

# Endlosschleife, damit der Befehl nicht endet und der Container beendet wird.
while true; do sleep 100; done


