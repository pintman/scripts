#!/bin/sh

for gitdir in */.git; 
do
  echo "-- $gitdir"
  git -C $gitdir/.. pull --prune
done

