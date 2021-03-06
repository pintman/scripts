#!/bin/sh

for d in $*;
do
    echo -en "=== $d (" $(git -C $d remote get-url origin) ") ==\n"
    #git -C $d log --format=format:"%cr %cn| %s";
    git -C $d log --stat --format=format:"%ar: %an| %s";
    find $d -type f -not -ipath *.git* -not -ipath *.idea* -exec wc -l {} \;
done
