
#!/bin/bash


set -xe

VENVDIR=~/tmp/venv

python3 -m venv $VENVDIR
. $VENVDIR/bin/activate

pip install ruff findlike

# -s Cause find to traverse the file hierarchies in lexicographical
# -order, i.e., alphabetical order within each directory.

# check if sorting option -s available (BSD) or not (GNU)
if find -s . -maxdepth 0 2>/dev/null; then
    SORT_OPT=-s
else
    SORT_OPT=""
fi

find \
     $SORT_OPT \
     . \
     -name "*py" \
     -exec ls {} ";" \
     -execdir ruff check -q {} ";" \
     > check.log

find $SORT_OPT . \
     -name "*py" \
     -exec echo "---- {}" ";" \
     -exec findlike \
       --show-scores --recursive \
       --filename-pattern "*py" --threshold 0.8 \
       --prefix "   " --hide-reference "{}" ";" \
     > similarities.log

