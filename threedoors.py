#!/usr/bin/env python
# -*- coding:utf-8 -*-
import random

def tdtest():
	doors = ['a', 'b', 'c']
	car = doors[random.randint(0, 2)]
	select = doors[random.randint(0, 2)]
	ledoors = list(filter(lambda x: x != select, doors))
	if car == select:
		select = ledoors[random.randint(0, 1)]
		if (select == car):
			return 'win'
	else:
		if (ledoors[0] != car):
			select = ledoors[1]
		else:
			select = ledoors[0]
		if (select == car):
			return 'win'
	return 'lose'

results = {'win' : 0, 'lose' : 0}
for i in range(2999):
	r = tdtest()
	results[r] = results[r] + 1

print('test 3000, win: %d; lose: %d' % (results['win'], results['lose']))