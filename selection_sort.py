#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


def selection_sort(rand_list):
	for position in range(0, len(rand_list)):
		min_position = find_min(rand_list, position)
		swap(rand_list, position, min_position)
		position += 1
	return rand_list


def find_min(rand_list, position):
	min_value = rand_list[position]
	min_index = position
	for i in range(position + 1, len(rand_list)):
		if rand_list[i] < min_value:
			min_value = rand_list[i]
			min_index = i
	return min_index


def swap(rand_list, position, new_position):
	rand_list[position], rand_list[new_position] = rand_list[new_position], rand_list[position]
	return True


def main():
	# generate random list
	list_len = randint(5, 20)
	rand_list = []
	while(list_len >= 0):
		rand_list.append(randint(0, 100))
		list_len -= 1
	print('List before selection sort alg:\n{}'.format(rand_list))
	print('List after selection sort alg:\n{}'.format(selection_sort(rand_list)))


if __name__ == '__main__':
	main()
