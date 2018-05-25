#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
	pass


L = MyList()
L.add(1)
print(L)
print(list)
L2 = list()
L2.add(2)

