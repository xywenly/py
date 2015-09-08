#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce
from collections import Iterator

# normalize name
def normalize(s):
	return s[0].upper() + s[1:].lower()

# prod a list of numbers
def prod(L):
	return reduce(lambda x, y: x * y, L)

# string to float
def str2float(s):
	s1, s2 = s.split('.')
	return str2int(s1) + str2dec(s2)

def char2num(s):
	return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]

def str2int(s):
	return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def str2dec(s):
	return reduce(lambda x, y: x * 0.1 + y, list(map(char2num, s))[::-1]) / 10

# test
L1 = list(map(normalize, ['aDm', 'JIM']));
print(L1)
print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
print(str2float('1234.0123699'))
