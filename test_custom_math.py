import unittest
import custom_math

class TestCustomMath(unittest.TestCase):

    
    def test_sum(self):
        self.assertEqual(custom_math.sum(1, 3), 4)

    
    def test_division_valid(self):
        self.assertEqual(custom_math.division(10, 2), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            custom_math.division(5, 0)


    def test_sum_multiple(self):
        test_values = [
            (1, 1, 2),
            (-1, 1, 0),
            (10, 15, 25)
        ]

        for x, y, expected in test_values:
            self.assertEqual(custom_math.sum(x, y), expected)

    def test_division_multiple(self):
        test_values = [
            (10, 2, 5),
            (20, 4, 5),
            (9, 3, 3)
        ]

        for x, y, expected in test_values:
            self.assertEqual(custom_math.division(x, y), expected)

    def test_positive_result(self):
        result = custom_math.sum(5, 5)
        self.assertTrue(result > 0)

    def test_negative_result(self):
        result = custom_math.sum(-5, -5)
        self.assertFalse(result > 0)

if __name__ == '__main__':
    unittest.main()