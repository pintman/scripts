#!/bin/sh

if [[ -z $MYSQL_ROOT_PW ]]; then
    echo "Specify a root passwort for mysql in env MYSQL_ROOT_PW";
    exit 1;
fi

# start docker and print port mappings

docker port $(docker run -e MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PW -d -P mysql)

echo Container running.
echo Connect to it with
echo mysql -P PORT -u root -p --protocol=TCP
