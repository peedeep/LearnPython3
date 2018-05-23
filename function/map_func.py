#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(x):
	return x * x


r = map(f, [1, 2, 3, 4, 5, 6])
print('r=', r)
print('list(r)=', list(r))


print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
