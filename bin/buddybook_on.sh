#!/bin/bash

# fail fast
set -o errexit

USAGE="Usage: $0 odt-file server"

FILE_ODT=${1?"ODT-File to be transferred is missing. $USAGE"}
FILE_PDF=$(basename $FILE_ODT .odt).pdf
SERVER=${2?"Server is missing. $USAGE"}
TGTDIR="/tmp"
OUTFILE=buddybook-$FILE_PDF

echo Copy $FILE_ODT to $SERVER:$TGTDIR
scp  $FILE_ODT $SERVER:$TGTDIR

echo Convert $TGTDIR/$FILE_ODT to $FILE_PDF on $SERVER
ssh $SERVER libreoffice --headless --convert-to pdf --outdir $TGTDIR $TGTDIR/$FILE_ODT

echo Convert to buddybook on server $SERVER
ssh $SERVER pdfjam-pocketmod $TGTDIR/$FILE_PDF --outfile $TGTDIR/$OUTFILE

echo copy result from $SERVER
scp $SERVER:$TGTDIR/$OUTFILE .

echo Removing files on $SERVER
ssh $SERVER rm $TGTDIR/$OUTFILE $TGTDIR/$FILE_ODT $TGTDIR/$FILE_PDF
