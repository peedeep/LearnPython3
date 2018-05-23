#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterator


b = isinstance([], Iterator)
print(b)
b = isinstance(iter([]), Iterator)
print(b)
b = isinstance(iter('abc'), Iterator)
print(b)
