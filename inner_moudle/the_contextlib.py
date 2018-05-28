#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contextlib import contextmanager, closing
from urllib.request import urlopen


with open('test.txt', 'r') as f:
	print(f.read())


class Query(object):


	def __init__(self, name):
		self.name = name


	def __enter__(self):
		print('Begin')
		return self

	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('End')
	

	def query(self):
		print('Query info about %s...' % self.name)


with Query('Rick') as q:
	q.query()


class Query(object):


	def __init__(self, name):
		self.name = name


	def query(self):
		print('Qeury info about %s...' % self.name)


@contextmanager
def create_query(name):
	print('Begin')
	q = Query(name)
	yield q
	print('End')


with create_query('Sophie') as q:
	q.query()


with closing(urlopen('https://www.python.org')) as page:
	for line in page:
		print(line)
