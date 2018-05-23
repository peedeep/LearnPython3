#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import functools

def now():
	print('2018-05-23')


f = now
f()


print(now.__name__)
print(f.__name__)


def log(func):
	def wrapper(*args, **kw):
		print('call %s:' % func.__name__)
		return func(*args, **kw)
	return wrapper


@log
def now():
	print('2018-05-24')


now()
print(now.__name__)


def log(text):
	def decorator(func):
		def wrapper(*args, **kw):
			print('%s %s:' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


@log('execute')
def now():
	print('2018-05-25')


now()
print(now.__name__)


print('####################### 分割线 ########################')


def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper


@log
def now():
	print('2018-05-26')


now()
print(now.__name__)


def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator


@log('execute')
def now():
	print('2018-05-26')


now()
print(now.__name__)










