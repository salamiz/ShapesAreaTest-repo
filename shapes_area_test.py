"""
Author:         Zulkifli Salami
Program:        shapes_area_test.py
Date Modified:  02-22-2023
Description:    Creates four functions to be tested in test_shapes.py: circle_area, ellipse_area,
trapezium_area, and rhombus_area. Each function will validate the data passed in before returning the calculated area
for the given shape.
"""
import math  # will have the math.class to be used
from math import pi  # allows direct use of math.pi with just pi

"""
shapes_area_test.py
TO DO: 
Validation for data type and raise TypeError
Validation for range and raise Value Error
Provide valuable error messages for the users
"""


def circle_area(radius):
    """ Calculates and returns the area of a circle """
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number.")
    elif radius < 0:
        raise ValueError("The radius can not be negative.")
    else:
        return pi * (math.pow(radius, 2))


def ellipse_area(major_radius, minor_radius):
    """ Calculates and returns the area of an ellipse """
    if type(major_radius) not in [int, float]:
        raise TypeError("The major radius must be a non-negative real number.")
    elif type(minor_radius) not in [int, float]:
        raise TypeError("The minor radius must be a non-negative real number.")
    elif major_radius < 0:
        raise ValueError("The major radius can not be negative.")
    elif minor_radius < 0:
        raise ValueError("The minor radius can not be negative.")
    else:
        return major_radius * minor_radius * pi


def trapezium_area(first_side, second_side, height):
    """ Calculates and returns the area of a trapezoid """
    if type(first_side) not in [int, float]:
        raise TypeError("The first side must be a non-negative real number.")
    elif type(second_side) not in [int, float]:
        raise TypeError("The second side must be a non-negative real number.")
    elif type(height) not in [int, float]:
        raise TypeError("The height must be a non-negative real number.")
    elif first_side < 0:
        raise ValueError("The first side can not be negative.")
    elif second_side < 0:
        raise ValueError("The second side can not be negative.")
    elif height < 0:
        raise ValueError("The height can not be negative.")
    else:
        return .5 * (first_side + second_side) * height


def rhombus_area(side, height):
    """ Calculates and returns the area of a rhombus """
    if type(side) not in [int, float]:
        raise TypeError("The side must be a non-negative real number.")
    elif type(height) not in [int, float]:
        raise TypeError("The height must be a non-negative real number.")
    elif side < 0:
        raise ValueError("The side can not be negative.")
    elif height < 0:
        raise ValueError("The height can not be negative.")
    return side * height
