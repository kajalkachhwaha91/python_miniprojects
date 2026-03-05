import unittest


def add(a, b):
    return a + b


def is_even(num):
    return num % 2 == 0


class TestMath(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_odd(self):
        self.assertFalse(is_even(5))


if __name__ == "__main__":
    unittest.main()
