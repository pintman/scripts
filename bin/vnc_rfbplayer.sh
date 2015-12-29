#!/bin/bash
# use -x for debugging

# destination for player
DIR=$(dirname $0)/vnc_rfbplayer

if [[ !( -d $DIR) ]]
then    
    mkdir $DIR
    # download vnc player application with curl
    curl http://www.tightvnc.com/download/RfbPlayer-1.4.0.1.zip > $DIR/vncp.zip
    # unzip into dest folder
    unzip -q -d $DIR $DIR/vncp.zip
    rm $DIR/vncp.zip
fi

# start player with given file
java -jar $DIR/RfbPlayer-1.4.0.1/RfbPlayer.jar URL file:$*

# findout more under http://www.tightvnc.com/rfbplayer.php

