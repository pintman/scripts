#!/bin/bash
# use -x for debugging

DIR=$(dirname $0)/vnc_viewer_jar

if [[ ! ( -d $DIR ) ]]
then
    mkdir $DIR
    # download vnc viewer application with curl
    curl http://www.tightvnc.com/download/1.3.10/tightvnc-1.3.10_javabin.zip > $DIR/vncv.zip
    # unzip into temp folder
    unzip -q -d $DIR $DIR/vncv.zip
    rm $DIR/vncv.zip
fi

# start viewer
#java -cp classes/VncViewer.jar VncViewer HOST localhost
java -cp $DIR/classes/VncViewer.jar VncViewer HOST localhost PORT 5901

