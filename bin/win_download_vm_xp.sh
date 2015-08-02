#!/bin/sh

# current dir and dir temp dir
CWD=$(pwd)
DIR=$(mktemp -d)

cd $DIR

# -O use filenames as suggested by the server
# -L follow http redirects to moved or changes locations
curl -O -L "https://www.modern.ie/vmdownload?browserOS=IE8-XP&parts=2&platform=Linux&virtPlatform=virtualbox&filename=VMBuild_20141027/VirtualBox/IE8/Linux/IE8.XP.For.Linux.VirtualBox.zip{.001,.002}"

cat IE8.XP.For.Linux.VirtualBox.zip.00* > combined.zip

unzip -d $CWD combined.zip

rm -rf $DIR
