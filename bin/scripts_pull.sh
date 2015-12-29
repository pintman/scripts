#!/bin/bash -x

DIR=$(dirname $0)

# -C run as if it were run there

git -C $DIR pull

