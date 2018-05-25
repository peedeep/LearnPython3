#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pickle


d = dict(name='Rick', age=20, score=88)
data = pickle.dumps(d)
print(data)


reborn = pickle.loads(data)
print(reborn)
