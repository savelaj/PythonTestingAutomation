from mathfun import add, multiply, power
import unittest


class TestStringMethods(unittest.TestCase):

    def test_add_commutative(self):
        self.assertEqual(add(15, 27), add(27, 15))

    def test_add_zero(self):
        self.assertEqual(add(0, 4), 4)
        self.assertEqual(add(7, 0), 7)

    def test_add_inverse(self):
        self.assertEqual(add(15, -15), 0)
        self.assertEqual(add(-23, 23), 0)

    def test_add_associative(self):
        left = add(add(1, 2), 3)
        right = add(1, add(2, 3))
        self.assertEqual(left, right)

    def test_multiply_commutative(self):
        self.assertEqual(multiply(15, 27), multiply(27, 15))

    def test_multiply_zero(self):
        self.assertEqual(multiply(0, 4), 0)
        self.assertEqual(multiply(7, 0), 0)

    def test_multiply_one(self):
        self.assertEqual(multiply(1, 4), 4)
        self.assertEqual(multiply(7, 1), 7)

    def test_multiply_associative(self):
        left = multiply(multiply(5, 2), 3)
        right = multiply(5, multiply(2, 3))
        self.assertEqual(left, right)

    def test_power_zero(self):
        self.assertEqual(power(65, 0), 1)

    def test_power_one(self):
        self.assertEqual(power(43, 1), 43)

    def test_power_power_mult(self):
        self.assertEqual(power(power(5, 6), 7), power(5, multiply(6, 7)))

    def test_power_add(self):
        self.assertEqual(power(6, add(3, 7)),
                         multiply(power(6, 3), power(6, 7)))


if __name__ == '__main__':
    unittest.main()
