#!/bin/sh

for d in $*;
do
    echo "=== $d ===";
    git -C $d remote get-url origin;
    git -C $d log --format=format:"%cr %cn| %s";
    find $d -type f -not -ipath *.git* -not -ipath *.idea* -exec wc -l {} \;
done
