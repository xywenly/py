#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import reduce

def normalize(str):
	return str[0].upper() + str[1:].lower();

def prod(L):
	return reduce(lambda x, y: x * y, L); 
	

L1 = list(map(normalize, ['aDm', 'JIM']));

print(L1)
print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
