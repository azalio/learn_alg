import unittest
from bisearch import *

class Test(unittest.TestCase):
    def test_is_prime(self):
        self.assertEqual(is_prime(3), True)
        self.assertEqual(is_prime(67), True)
        self.assertEqual(is_prime(-1), False)

    def test_gen_prime(self):
        self.assertTrue(isinstance(gen_prime(10), list))
        self.assertFalse(gen_prime(1))

    def test_bi_search(self):
        a = gen_prime(300)
        self.assertFalse(bi_search(1, a))
        self.assertFalse(bi_search(2000, a))
        self.assertEqual(bi_search(2, a), 0)
        self.assertEqual(bi_search(67, a), 18)
        self.assertEqual(bi_search(68, a), 19)


if __name__ == '__main__':
    unittest.main()
