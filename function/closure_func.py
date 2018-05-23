#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""闭包:
我们在函数lazy_sum中又定义了函数sum，
并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
这种称为“闭包（Closure）”的程序结构拥有极大的威力。
"""

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum


f = lazy_sum(1, 3, 5, 7, 9)
print('f=', f)
print('f()=', f())
f1 = lazy_sum(1, 3, 5, 7, 9)
print(f == f1)


def count():
	fs = []
	for i in range(1, 4):
		def f():
			print('i * i=', i * i)
			return i * i
		fs.append(f)
	return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


def count():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs


f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())
