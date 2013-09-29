#!/bin/bash 
if [ "$2" ]; then
    grep -n -r "$1" . | grep -v "$2" |grep "$1" --color=auto
else
    grep -n -r "$1" . |grep "$1" --color=auto
fi
