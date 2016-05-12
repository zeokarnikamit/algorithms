# -*- coding: utf-8 -*-
__author__ = "karnikamit"
"""
    Counting Sort
    -------------
    Time complexity: O(n+k) - k = range of values
"""


def counting_sort(array):
    max_value = 0
    for m in array:
        if m > max_value:
            max_value = m
    n, m = len(array), max_value + 1
    count = [0] * m     # initialize with zeros
    for i in array:
        count[i] += 1
    j = 0
    for a in xrange(m):
        for c in xrange(count[a]):
            array[j] = a
            j += 1
    return array
