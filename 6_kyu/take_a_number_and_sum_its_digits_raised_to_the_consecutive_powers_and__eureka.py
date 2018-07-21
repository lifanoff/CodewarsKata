#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!:
https://www.codewars.com/kata/5626b561280a42ecc50000d1"""


def sum_dig_pow(a, b):
    return filter(lambda x: x == sum(int(str(x)[i]) ** (i + 1) for i in range(len(str(x)))), range(a, b + 1))
