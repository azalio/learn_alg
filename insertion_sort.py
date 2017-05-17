#!/usr/bin/env python
from random import randint


def insert(arr, index, value):
    while(index>=0 and arr[index] > value):
        arr[index+1] = arr[index]
        index -= 1
    arr[index+1] = value


def ins_sort(arr):
    for i in range(1, len(arr)):
        insert(arr, i-1, arr[i])
    return arr


def main():
    #gen test array
    len_ = randint(10, 20)
    arr = []
    while len_ >= 0:
        arr.append(randint(1, 100))
        len_ -= 1
    print("Array before insertion sort:\n{}".format(arr))
    print("Array after insertion sort:\n{}".format(ins_sort(arr)))


if __name__ == '__main__':
    main()
