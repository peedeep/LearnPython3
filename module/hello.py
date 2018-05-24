#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'a test module'

__author__ = 'Rick'

import sys


def test():
	print('path: ', sys.path)
	args = sys.argv
	if len(args) == 1:
		print('Hello word!')
	elif len(args) == 2:
		print('Hello %s!' % args[1])
	else:
		print('Too many arguments!')


if __name__  == '__main__':
	test()
