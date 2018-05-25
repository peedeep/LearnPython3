#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json


d = dict(nam='Rick', age = 3, score=88)
print(json.dumps(d))


json_str = '{"age":20, "score":88, "name":"Rick"}'
print(json.loads(json_str))


class Student(object):


	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score


def student2dict(std):
	return {
			'name': std.name, 'age': std.age, 'score': std.score
			}


def dict2student(d):
	return Student(d['name'], d['age'], d['score'])



s = Student('Rick', 20, 88)
print(json.dumps(student2dict(s)))
print(json.dumps(s, default=lambda obj : obj.__dict__))
print(json.loads(json_str, object_hook=dict2student))






