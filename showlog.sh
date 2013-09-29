#!/bin/bash
tail -100 $HOME/doc/work/logs/error.log| grep --color=auto -P '_\[.*?\]_'

