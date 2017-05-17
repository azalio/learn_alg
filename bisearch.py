#!/usr/bin/env python
import math
import random


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0 and num > 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def gen_prime(num):
    if num <= 1:
        return False
    prime = []
    for i in range(2, num):
        if is_prime(i):
            prime.append(i)

    return prime


def bi_search(rand_int, prime_numbers):
    if rand_int <= 1:
        return False
    if rand_int > prime_numbers[-1]:
        return False
    min_ = 0
    max_= len(prime_numbers) - 1
    guess = -1
    while(prime_numbers[guess] != rand_int):
        if min_ > max_:
            return min_
        guess = ( min_ + max_ )/2
        if prime_numbers[guess] == rand_int:
            return guess
        elif prime_numbers[guess] < rand_int:
            min_ = guess + 1
        else:
            max_ = guess - 1

if __name__ == "__main__":

    prime_numbers = gen_prime(300)
    print(prime_numbers)
    rand_int = random.randint(2, 300)
    length = bi_search(rand_int, prime_numbers)
    print("Before {} {} numbers".format(rand_int, length))
