#!/bin/bash

GITDIR=$(dirname "$0")

echo "Updating $GITDIR"
git -C "$GITDIR" pull
