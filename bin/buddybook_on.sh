#!/bin/bash

USAGE="Usage: $0 file server"

FILE=${1?"File to be transferred is missing. $USAGE"}
SERVER=${2?"Server is missing. $USAGE"}
TGTDIR="/tmp"
OUTFILE=pocketmod-$FILE

echo Copy $FILE to $SERVER
scp  $FILE $SERVER:$TGTDIR
echo Convert on server $SERVER
ssh $SERVER pdfjam-pocketmod $TGTDIR/$FILE --outfile $TGTDIR/$OUTFILE
echo copy result from $SERVER
scp $SERVER:$TGTDIR/$OUTFILE .
echo Removing result $OUTFILE on server $SERVER
ssh $SERVER rm $TGTDIR/$OUTFILE
