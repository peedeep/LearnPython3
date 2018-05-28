#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))


Circle = namedtuple('Circle', ['x', 'y', 'z'])
print(Circle)


q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)


dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])


print(dict([('a', 1), ('b', 2), ('c', 3)]))
print(OrderedDict([('a', 1), ('b', 2), ('c', 3)]))


od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))


c = Counter()
for ch in 'programming':
	c[ch] = c[ch] + 1
print(c)
