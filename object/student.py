#!/usr/bin/env python3
# -*- coding: utf-8 -*-


std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }


def print_score(std):
	print('%s: %s' % (std['name'], std['score']))


print_score(std1)
print('================')
print_score(std2)
print('================')

class Student(object):


	def __init__(self, name, score):
		self.name = name
		self.score = score

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

	
	def print_score(self):
		print('%s: %s' % (self.name, self.score))



bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)

bart.print_score()
print(bart.name)
print(bart.get_grade())
lisa.print_score()
print(lisa.name)
print(lisa.get_grade())
print('================')


class Animal(object):


	def __init__(self, name, age):
		self.__name = name
		self._age = age


tom = Animal('Tom', 3)
print(tom._age)
print(tom._Animal__name)
print(tom.__name)
