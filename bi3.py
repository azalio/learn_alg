# -*- coding: utf-8 -*-

arr = [-1, 1, 2, 3, 5]

def bisearch2(arr, param):
    l = 0
    r = len(arr)
    if r == 0 or param < arr[0] or param > arr[-1]:
        return None
    while r - l > 1:
        m = (r + l)//2
        if param >= arr[m]:
            l = m
        else:
            r = m
    return l if arr[l] == param else None

assert bisearch2(arr, 30) is None, None
assert bisearch2(arr, -2) is None, None
assert bisearch2(arr, -1) == 0, 0
assert bisearch2(arr, 5) == 4, 4
assert bisearch2(arr, 1) == 1, 1

arr = []
assert bisearch2(arr, 1) is None, None

arr = [0]
assert bisearch2(arr, 0) == 0, 0