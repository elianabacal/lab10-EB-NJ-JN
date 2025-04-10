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
        self.assertEqual(subtract(1,2), 2)
        self.assertEqual(subtract(2,2), 1)
        self.assertEqual(subtract(3,2), 1)
    ##########################

    # Partner 1
    def test_multiply(self): # 3 assertions
        pass

    def test_divide(self): # 3 assertions
        pass
    ##########################

    # Partner 2
    def test_divide_by_zero(self): # 1 assertion
        self.assertRaises(ZeroDivisionError)
        #     div(0, 5)


    def test_logarithm(self): # 3 assertions
        self.assertEqual(math.log(8,2), 0)
        self.assertEqual(math.log(1,2), 0)
        self.assertEqual(math.log(1,1), 1)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        self.assertRaises(ValueError)
    ##########################
    
    # Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        pass

    def test_hypotenuse(self): # 3 assertions
        pass

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        pass
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()