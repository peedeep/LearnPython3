#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from types import MethodType


class Student(object):
	pass


s = Student()
s.name = "Rick"
print(s.name)


def set_age(self, age):
	self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(26)
print(s.age)


def set_score(self, score):
	self.score = score


Student.set_score = set_score
s.set_score(99)
print(s.score)


class Student(object):
	__slots__ = ('name', 'age')


s = Student()
s.name = "Sophie"
s.age = 25
# s.score = 66


class GraduateStudent(Student):
	pass


g = GraduateStudent()
g.score = 98
print(g.score)

