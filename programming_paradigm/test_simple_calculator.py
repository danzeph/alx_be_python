import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Creating an instance(Object) of the class for use"""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test additon function"""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(1, -1), 0)
        self.assertEqual(self.calc.add(0, -0), 0)
        
    def test_subtration(self):
        """Test subtraction Function"""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(0, -1), 1)
        self.assertEqual(self.calc.subtract(4, -7), 11)
        
    def test_multiplication(self):
        """Test multiplication function"""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(0, -1), 0)
        self.assertEqual(self.calc.multiply(-4, -2), 8)
        
    def test_divide(self):
        """"Test division funciton"""
        self.assertEqual(self.calc.divide(4, 2), 2)
        self.assertEqual(self.calc.divide(-2,-2), 1)
        self.assertEqual(self.calc.divide(-15, 5), -3)
        self.assertEqual(self.calc.divide(0, -2), 0)
        """Division by zero handled in the simple_calculator to return None"""
        self.assertEqual(self.calc.divide(8, 0), None)
        
    # def test_divide_by_zero(self):
    #     """Test division by zero raises error"""
    #     with self.assertRaises(ValueError):
    #         self.calc.divide(10, 0) 
        
if __name__ == '__main__':
    unittest.main()
