import unittest
from palindrome import *


class Test(unittest.TestCase):
    def setUp(self):
        self.word = 'neveroddoreven'

    def test_word_is_palindrome(self):
        self.assertTrue(word_is_palindrome(self.word))

    def test_rec_word_is_palindrome(self):
        self.assertTrue(rec_word_is_palindrome(self.word))
