#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re


m = re.split(r'[\s\,\;]+', 'a,b;; c d')
print(m)

m1 = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(m1)

m2 = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m2)
print(m2.group(0))
print(m2.group(1))
print(m2.group(2))


print(re.match(r'^(\d+)(0*)$', '102300').groups())
print(re.match(r'^(\d+?)(0*)$', '102300').groups())

