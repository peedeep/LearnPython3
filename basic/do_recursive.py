#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
    fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return face_iter(num - 1, num * product)
