#!/bin/bash

PASS=geheimnis

USERS=$(cat << EOF
ita1
ita2
ita3
EOF
)

echo Adding users with password $PASS

for u in $USERS; 
do
  groupadd $u
  useradd -m -g $u -s /bin/bash $u
  bash -c "echo $u:$PASS | chpasswd"
  echo $u added
done
