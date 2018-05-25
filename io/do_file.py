#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os


print('os.name', os.name)
print('os.uname', os.uname())
print('os.environ', os.environ)
print('os.environ.get path', os.environ.get('PATH'))
print('os.environ.get x', os.environ.get('x', 'default'))
print('=======================')


print('abspath', os.path.abspath('.'))
print('join', os.path.join('/Users/root', 'testdir'))
print('mkdir', os.mkdir('testdir'))
print('rmdir', os.rmdir('testdir'))
print('=======================')

print(open('test.txt', 'w').close())
print('os.rename', os.rename('test.txt', 'test.py'))
print('os.remove', os.remove('test.py'))


print([x for x in os.listdir('.') if os.path.isdir(x)])
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
