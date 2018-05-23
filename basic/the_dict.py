#!/usr/bin/env python3
# -*-coding: utf-8 -*-


numbers = {
    'one': 1,
    'two': 2,
    'three': 3
}

names = {'肥肥':1, '张健珍':'Sophie', '曹浩平':'Rick'}


print('numbers[\'one\']', numbers['one'])
print('numbers.get(\'four\', 4)', numbers.get('four', 4))

for name in names:
    print('name is %s, eng is %s' % (name, names.get(name)))
    print('name is %s, eng is %s' % (name, names[name]))



