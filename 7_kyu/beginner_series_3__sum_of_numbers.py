#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Beginner Series #3 Sum of Numbers: https://www.codewars.com/kata/55f2b110f61eb01779000053"""


def get_sum(a, b):
    return sum(range(min([a, b]), max([a, b]) + 1))
