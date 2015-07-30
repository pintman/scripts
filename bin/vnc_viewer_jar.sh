#!/bin/bash
# use -x for debugging

TMP=$(mktemp -d)

# download vnc viewer application with curl
curl http://www.tightvnc.com/download/1.3.10/tightvnc-1.3.10_javabin.zip > $TMP/vncv.zip
# unzip into temp folder
unzip -q -d $TMP $TMP/vncv.zip

# start viewer
#java -cp classes/VncViewer.jar VncViewer HOST localhost
java -cp $TMP/classes/VncViewer.jar VncViewer HOST localhost PORT 5901


rm -rf $TMP
