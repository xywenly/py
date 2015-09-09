#!/usr/bin/env python
# -*- coding:utf-8 -*-

with open('/home/wenly/Documents/py/readme.txt', 'r') as f:
	#print(f.read())
	for line in f.readlines():
		print(line.strip())
		
with open('/home/wenly/Documents/py/iotest.txt', 'w') as f:
	f.write('Hello, world.\n')
	f.write('more...')