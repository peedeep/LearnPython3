#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable


print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))
