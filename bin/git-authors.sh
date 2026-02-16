#!/bin/sh

# for the given git Repo, list authors and the number of commits.

if [[ -z $* ]]; then
   echo "No Repo given."
   exit 1
fi

echo -e "num commits     author"
echo    "-----------     ------"
git -C $* log | grep 'Author:' | sort | uniq -c

