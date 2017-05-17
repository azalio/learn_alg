#!/usr/bin/env python
# -*- coding: utf-8 -*-


def word_is_palindrome(word):
    if word == "" or len(word) == 1:
        return True
    for i in range(0, len(word) / 2 + 1):
        if word[i] != word[0 - i - 1]:
            return False
    return True


def rec_word_is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    else:
        return rec_word_is_palindrome(word[1:-1])


def main():
    # print "Please, enter word:",
    # word = raw_input()
    word = "abcdcba"

    if word_is_palindrome(word):
        print("Word: {} is palindrome".format(word))
    else:
        print("Word: {} is not palindrome".format(word))

    if rec_word_is_palindrome(word):
        print("Word: {} is palindrome".format(word))
    else:
        print("Word: {} is not palindrome".format(word))


if __name__ == "__main__":
    main()
