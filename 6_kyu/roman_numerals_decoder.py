#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Roman Numerals Decoder: https://www.codewars.com/kata/51b6249c4612257ac0000005"""

data = [
    ('CM', 900),
    ('CD', 400),
    ('XC', 90),
    ('XL', 40),
    ('IX', 9),
    ('IV', 4),
    ('M', 1000),
    ('D', 500),
    ('C', 100),
    ('L', 50),
    ('X', 10),
    ('V', 5),
    ('I', 1)
]


def solution(roman):
    arab = 0

    while len(roman) > 0:
        for x in data:
            if roman.startswith(x[0]):
                arab += x[1]
                roman = roman[len(x[0]):]
                break

    return arab
