#!/usr/bin/env python3
# -*- coding: utf-8 -*-


words = ['今天', '天气', '怎么样', '?']
for word in words:
    print(word)


for x in range(15):
    print('number: ', x)
    print('num is: %d, num * num is: %d' % (x, x * x))


d = {'one': 1, 'two': 2, 'three': 3}
for k, v in d.items():
    print(k, v)
