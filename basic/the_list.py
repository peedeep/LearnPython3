#!/usr/bin/env python3
# -*- coding: utf-8 -*-


names = ['Rick', 'Sophie', 'Fei']
print('names=', names)
print('len(names)=', len(names))
print('names[0]', names[0])
print('names[1]', names[1])
print('names[2]', names[2])
names.pop()
print('names=', names)


L = [x * x for x in range(1, 10)]
print(L)


L = [x * x for x in range(1, 10) if x % 2 == 0]
print(L)


print([m + n for m in 'ABC' for n in 'XYZ'])


L = ['I', 'm', 'CHP']
print([s.lower() for s in L])

