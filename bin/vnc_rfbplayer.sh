#!/bin/bash
# use -x for debugging

TMP=$(mktemp -d)

# download vnc player application with curl
curl http://www.tightvnc.com/download/RfbPlayer-1.4.0.1.zip > $TMP/vncp.zip
# unzip into temp folder
unzip -q -d $TMP $TMP/vncp.zip

# start player with given file
java -jar $TMP/RfbPlayer-1.4.0.1/RfbPlayer.jar URL file:$*

# findout more under http://www.tightvnc.com/rfbplayer.php

# remove the temp dir
rm -rf $TMP
