# -*- coding: utf-8 -*-


arr = [-1, 1, 2, 3, 5]


def bisearch2(arr, param):
    l = 0
    r = len(arr)
    if r == 0 or arr[0] > param or arr[-1] < param:
        return None

    while r - l > 1:
        m = (l + r)//2
        if param >= arr[m]:
            l = m
        else:
            r = m
        # print("l = {} r = {}, m = {}".format(l, r, m))
    return l if arr[l] == param else None


# print(bisearch2(arr, 30))
assert bisearch2(arr, 30) is None, None
assert bisearch2(arr, -2) is None, None
assert bisearch2(arr, -1) == 0, 0
assert bisearch2(arr, 5) == 4, 4
assert bisearch2(arr, 1) == 1, 1


arr = []
assert bisearch2(arr, 1) is None, None

arr = [0]
assert bisearch2(arr, 0) == 0, 0




