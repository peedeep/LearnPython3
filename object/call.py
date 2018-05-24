#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):


	def __init__(self, name):
		self.name = name


	def __call__(self):
		print('My name is %s ' % self.name)


s = Student('Rick')
s()


print(callable(Student('Sophie')))
print(callable(s))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

