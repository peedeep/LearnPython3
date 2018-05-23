#!/usr/bin/env python3
# -*- coding: utf-8 -*-


g = (x * x for x in range(1, 10))
print('g', g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))


g = (x * x for x in range(1, 10))
for n in g:
	print(n)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		print(b)
		a, b = b, a + b
		n = n + 1
	return 'done'
fib(10)


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1
	return 'done'
f = fib(10)
print(f)
