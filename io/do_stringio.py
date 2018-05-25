#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from io import StringIO


f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
print(f.getvalue())


f = StringIO('hello rick! \n hello Sophie!')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())



