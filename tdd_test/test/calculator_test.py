import unittest
import tdd_test.src.calculator

class CalculatorTest(unittest.TestCase):
    def test_foo(self):
        calculator = Calculator()
        self.assertEqual(2, 2)

if __name__ == '__main__':
    unittest.main()
