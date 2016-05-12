# -*- coding: utf-8 -*-
__author__ = "karnikamit"
"""
    Bucket sort/ Bin sort
    ---------------------

    is a distribution sort that works by arranging elements into several ‘buckets’
    which are then sorted using another sort,
    typically insertion sort, and merged into a sorted list.
    Time complexity - O (n+k) : n - number of elements, k - number of buckets

"""
from math import sqrt
from insertion_sort import sort as insertion_sort


def hashing(a_list):
    no = a_list[0]
    for i in xrange(1, len(a_list)):
        if no < a_list[i]:
            no = a_list[i]
    return [no, int(sqrt(len(a_list)))]


def re_hashing(i, code):
    return int(i / code[0] * (code[1] - 1))


def bucket_sort(array):
    sorted_array = []
    code = hashing(array)
    if code:
        temp_buckets = [[] for _ in xrange(code[1])]
        print len(temp_buckets)

        for k in array:
            x = re_hashing(k, code)
            b = temp_buckets[x]
            b.append(k)

        buckets = [insertion_sort(bucket) for bucket in temp_buckets]

        # merge the buckets: O(n)
        [sorted_array.extend(k) for k in buckets]
    return sorted_array
