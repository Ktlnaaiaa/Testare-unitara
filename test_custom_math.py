import unittest
import custom_math

class TestCustomMath(unittest.TestCase):
    def test_sum_multiple(self):
        test_values = [
            (1, 1, 2),
            (-1, 1, 0),
            (10, 15, 25)
        ]

        for x, y, expected in test_values:
            self.assertEqual(custom_math.sum(x, y), expected)

    def test_division(self):
        self.assertEqual(custom_math.division(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            custom_math.division(5, 0)

if __name__ == '__main__':
    unittest.main()