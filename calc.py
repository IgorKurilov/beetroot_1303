import unittest

class Calc:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def power(a, b):
        return a ** b

    @staticmethod
    def div(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    @staticmethod
    def floor_div(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a // b

    @staticmethod
    def mod(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a % b

class TestCalcMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calc.add(3, 4), 7)

    def test_sub(self):
        self.assertEqual(Calc.sub(5, 2), 3)

    def test_mul(self):
        self.assertEqual(Calc.mul(3, 4), 12)

    def test_power(self):
        self.assertEqual(Calc.power(2, 3), 8)

    def test_div(self):
        self.assertEqual(Calc.div(10, 2), 5)
        with self.assertRaises(ValueError):
            Calc.div(10, 0)

    def test_floor_div(self):
        self.assertEqual(Calc.floor_div(10, 3), 3)
        with self.assertRaises(ValueError):
            Calc.floor_div(10, 0)

    def test_mod(self):
        self.assertEqual(Calc.mod(10, 3), 1)
        with self.assertRaises(ValueError):
            Calc.mod(10, 0)

if __name__ == '__main__':
    unittest.main()
