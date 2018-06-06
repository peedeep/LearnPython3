#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def consumer():
	r = ''
	while True:
		n = yield r
		if not n:
			print('Consuming not n: %s' % n)
			return 
		print('Consuming %s...' % n)
		r = '200 OK'


def produce(c):
	c.send(None)
	n = 0
	while n < 5:
		n = n + 1
		print('Producing %s...' % n)
		r = c.send(n)
		print('Consumer return: %s' % r)
	c.close()


c = consumer()
produce(c)
