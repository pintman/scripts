#!/bin/bash

. freifunk_common

exec_ff "swconfig dev switch0 show|grep link"
