#!/usr/bin/env python3
# -*- coding: utf-8 -*-


with open('../README.md', 'r') as f:
	print(f.read())


with open('../README.md', 'w') as f:
	f.write('learn \n python3')


with open('../README.md', 'r') as f:
	for line in f.readlines():
		print(line.strip())



