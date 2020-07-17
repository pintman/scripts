#!/bin/sh

# Output the given git folders in order of the last commit.
#
for d in $*; do 
    # format options in section PRETTY FORMATS in git log's man page.
    test -d $d/.git && git -C $d log -n 1 --format="%ci $d" ;  
done | sort
