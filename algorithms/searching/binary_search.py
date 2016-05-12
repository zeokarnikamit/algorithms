"""
    Binary Search
    -------------
    Recursively partitions the list until the `key` is found.

    Time Complexity:  O(lg n)

    Psuedo Code: http://en.wikipedia.org/wiki/Binary_search

"""
from algorithms.sorting.quick_sort import sort as quick_sort


def search(seq, key):
    """
    Takes a list of integers and searches if the `key` is contained within
    the list.

    :param seq: A list of integers
    :param key: The integer to be searched for
    :rtype: The index of where the `key` is located in the list. If `key` is
            not found then False is returned.
    """

    lo = 0
    hi = len(seq) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False


def binary_search(array, value):
    array = quick_sort(array)
    low = 0
    high = len(array) - 1
    while high >= low:
        mid = (high - low) / 2
        if array[mid] > value:
            high = mid - 1
        elif array[mid] < value:
            low = mid + 1
        else:
            return mid
    return False
