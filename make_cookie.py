#!/usr/bin/env python
#coding:utf-8

import sys
import commands
cookie_file = sys.argv[1]
a = commands.getstatusoutput("sed -i '/✓/d' %s" %cookie_file)
with open(cookie_file, 'r') as f:
    cookies = f.readlines()
last_cookies = {}
key = None
for i, v in enumerate(cookies):
    sig = i % 6
    if sig == 0:
        key = v.replace('\n', '')
    elif sig == 1:
        last_cookies[key] = v.replace('\n','')
print last_cookies
