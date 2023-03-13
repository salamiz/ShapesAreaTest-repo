"""
# Author:         Zulkifli Salami
# Program:        Test Cases for shapes
# Date Created:   02-22-23
# Date Modified:  02-22-23
# Description:
""""""
test_shapes_Zulkifli.py
TO DO:
create TestCasesShapes
Use all of the following methods:
setUpClass
tearDownClass
setUp
tearDown
"""
# import unittest
import unittest
# import shapes.py
from app.shapes_area_test import *
# import pi
import math
from math import pi


class TestCaseZulkifli(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Set up class")

    @classmethod
    def tearDownClass(cls):
        print("Tear down class")

    def setUp(self):
        print("Set up")

    def tearDown(self):
        print("Tear down\n")

    """
    test_area_circle_positive_values
    test_area_circle_negative_values
    test_area_circle_misc_values
    """

    def test_area_circle_positive_values(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * (math.pow(2.1, 2)))

    def test_area_circle_negative_values(self):
        with self.assertRaises(ValueError):
            circle_area(-2)

    def test_area_circle_misc_values(self):
        with self.assertRaises(TypeError):
            circle_area("Thirty")
        with self.assertRaises(TypeError):
            circle_area(True)

    """
    test_area_ellipse_positive_values
    test_area_ellipse_negative_values
    test_area_ellipse_misc_values
    """

    def test_area_ellipse_positive_values(self):
        self.assertAlmostEqual(ellipse_area(9, 3), 9*3*pi)
        self.assertAlmostEqual(ellipse_area(6.139, 3.09), 6.139 * 3.09 * pi)
        self.assertAlmostEqual(ellipse_area(12.139, 10), 12.139 * 10 * pi)

    def test_area_ellipse_negative_values(self):
        with self.assertRaises(ValueError):
            ellipse_area(-16, 9)
        with self.assertRaises(ValueError):
            ellipse_area(-12, -8)
        with self.assertRaises(ValueError):
            ellipse_area(12, -5.67)

    def test_area_ellipse_misc_values(self):
        with self.assertRaises(TypeError):
            ellipse_area(-16, "9.0r")
        with self.assertRaises(TypeError):
            ellipse_area("12%", True)
        with self.assertRaises(TypeError):
            ellipse_area(12, False)

    """
    test_area_trapezium_positive_values
    test_area_trapezium_negative_values
    test_area_trapezium_misc_values
    """

    def test_area_trapezium_positive_values(self):
        self.assertAlmostEqual(trapezium_area(45.9, 30, 12), .5 * (45.9 + 30) * 12)
        self.assertAlmostEqual(trapezium_area(61.39, 30.9, 21.98), .5 * (61.39 + 30.9) * 21.98)
        self.assertAlmostEqual(trapezium_area(61, 30.9, 11), .5 * (61 + 30.9) * 11)

    def test_area_trapezium_negative_values(self):
        with self.assertRaises(ValueError):
            trapezium_area(-34.9, 17, 8)
        with self.assertRaises(ValueError):
            trapezium_area(-12, -8, -3)
        with self.assertRaises(ValueError):
            trapezium_area(12, -8.95, -3)

    def test_area_trapezium_misc_values(self):
        with self.assertRaises(TypeError):
            trapezium_area(-16, 9.0, False)
        with self.assertRaises(TypeError):
            trapezium_area("12c", pi, 30)
        with self.assertRaises(TypeError):
            trapezium_area(12, "Thirty", 30)

    """
    test_area_rhombus_positive_values
    test_area_rhombus_negative_values
    test_area_rhombus_misc_values
    """

    def test_area_rhombus_positive_values(self):
        self.assertAlmostEqual(rhombus_area(0.34, 3.098), 0.34*3.098)
        self.assertAlmostEqual(rhombus_area(21, 9.87), 21*9.87)
        self.assertAlmostEqual(rhombus_area(21.094783, 9), 21.094783 * 9)

    def test_area_rhombus_negative_values(self):
        with self.assertRaises(ValueError):
            rhombus_area(-54, -5.753)
        with self.assertRaises(ValueError):
            rhombus_area(32, -29.05)
        with self.assertRaises(ValueError):
            rhombus_area(-32, 29)

    def test_area_rhombus_misc_values(self):
        with self.assertRaises(TypeError):
            rhombus_area(-16, "9.0r")
        with self.assertRaises(TypeError):
            rhombus_area("12%", True)
        with self.assertRaises(TypeError):
            rhombus_area("12%", 12)


# Run the test cases
if __name__ == '__main__':
    unittest.main()
