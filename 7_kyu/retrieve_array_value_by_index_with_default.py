#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Retrieve array value by index with default: https://www.codewars.com/kata/515ceaebcc1dde8870000001"""


def solution(items, index, default_value):
    try:
        return items[index]
    except IndexError:
        return default_value
