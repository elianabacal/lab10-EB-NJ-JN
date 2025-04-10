#https://github.com/elianabacal/lab10-EB-NJ-JN.git
#partner 1 eliana
#partner 2 Neha
import unittest
from calculator import *



class TestCalculator(unittest.TestCase):
    # Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1,2), 3)
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(3,3), 6)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(4,2), 2)
        self.assertEqual(subtract(2,2), 0)
        self.assertEqual(subtract(3,2), 1)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,2), 6)
        self.assertEqual(mul(-2, -2), 4)
        self.assertEqual(mul(3,4), 12)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(5,5), 1)
        self.assertEqual(div(2,6), 3)
        self.assertEqual(div(2,10), 5)


    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(math.log(8,2), 3)
        self.assertEqual(math.log(1,2), 0)
        self.assertEqual(math.log(2,2), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0,1)
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)


    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(10,5), 11.180339887498949)
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(7, 7), 9.899494936)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            math.sqrt(-1)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(4), 2)

# Do not touch this
if __name__ == "__main__":
    unittest.main()