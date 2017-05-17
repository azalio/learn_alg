# -*- coding: utf-8 -*-


def partition(arr, start, end):
    pindex = start
    pivot = arr[end]
    for i in range(start, end):
        if arr[i] <= pivot:
            arr[i], arr[pindex] = arr[pindex], arr[i]
            pindex += 1
    arr[pindex], arr[end] = arr[end], arr[pindex]
    return pindex


def quicksort(arr, start, end):
    if start > end:
        return
    pindex = partition(arr, start, end)
    quicksort(arr, start, pindex-1)
    quicksort(arr, pindex+1, end)
    return arr

arr = [7,2,1, -1, 23, 54, -5, 23, 33]
print(arr)
print(quicksort(arr,0,len(arr)-1))

