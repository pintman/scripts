#!/bin/sh

for gitdir in */.git/refs/remotes; 
do
  d=$gitdir/../../../
  echo "-- $d"
  git -C $d pull --prune
done

