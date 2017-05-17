import unittest
from selection_sort import *

class Test(unittest.TestCase):
    def setUp(self):
        self.a = [2, 71, 61, 66, 58, 25, 86, 41, 5, 68]

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.a), [2, 5, 25, 41, 58, 61, 66, 68, 71, 86])

    def test_find_min(self):
        self.assertEqual(find_min(self.a, 1), 8)

    def test_swap(self):
        swap(self.a, 0, 1)
        self.assertEqual(self.a, [71, 2, 61, 66, 58, 25, 86, 41, 5, 68])


if __name__ == '__main__':
    unittest.main()
