#!/bin/bash

PASS=geheimnis

USERS=$(cat << EOF
username1
username2
username3
EOF
)

echo Adding users with password $PASS

for u in $USERS; 
do
  useradd -m -s /bin/bash $u
  bash -c "echo $u:$PASS | chpasswd"
  echo $u added
done
