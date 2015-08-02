#!/bin/sh

# current dir and dir temp dir
CWD=$(pwd)
DIR=$(mktemp -d)

cd $DIR

# -O use filenames as suggested by the server
# -L follow http redirects to moved or changes locations
curl -O -L "https://www.modern.ie/vmdownload?browserOS=IE11-Win7&parts=4&platform=Linux&virtPlatform=virtualbox&filename=VMBuild_20141027/VirtualBox/IE11/Linux/IE11.Win7.For.Linux.VirtualBox.zip{.001,.002,.003,.004}"

cat IE11.Win7.For.Linux.VirtualBox.zip.00* > combined.zip

unzip -d $CWD combined.zip

rm -rf $DIR
