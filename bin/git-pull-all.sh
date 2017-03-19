#!/bin/sh

find $* -maxdepth 0 -type d -print -exec git -C {} pull \;
