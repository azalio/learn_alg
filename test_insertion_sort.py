import unittest
from insertion_sort import *


class Test(unittest.TestCase):
    def setUp(self):
        self.a = [2, 71, 61, 66, 58, 25, 86, 41, 5, 68]

    def test_ins_sort(self):
        self.assertEqual(ins_sort(self.a), [2, 5, 25, 41, 58, 61, 66, 68, 71, 86])

    def test_insert(self):
        insert(self.a, 3, 58)
        self.assertEqual(self.a, [2, 58, 71, 61, 66, 25, 86, 41, 5, 68])


if __name__ == '__main__':
    unittest.main()
