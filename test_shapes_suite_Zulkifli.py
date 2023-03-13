"""
# Author:         Zulkifli Salami
# Program:        Test Cases for shapes suite
# Date Created:   02-22-23
# Date Modified:  02-22-23
# Description:""""""
# test_shapes_suite_Zulkifli.py
# TO DO: 
# 
# The function will offer the user a menu to run the tests on the area functions for a circle, trapezium, ellipse, 
#     rhombus, or quit.
# As long as the user does not select to quit, the menu will keep prompting after running the tests
# The function will make use of the TestSuite() class
# The user should be able to enter upper- or lowercase letters for the menu, and their entry should have extra spaces
#     removed using strip() and validated
# """

# import unittest
import unittest
# import TestCaseShapes
from test_shapes_Zulkifli import TestCaseZulkifli


def menu():
    """ Function to prompt for and return user menu selection for test_shapes_Zulkifli.py testing suite """
    menu_prompt = """\nPlease enter one of the following options:
        - 'c' for testing area of circle
        - 't' for testing area of trapezium
        - 'e' for testing area of ellipse
        - 'r' for testing area of rhombus
        - 'q' to quit What would you like to do: 
        """

    # Get a selection from the user
    return input(menu_prompt).strip().lower()


# Create a user-friendly test suite using a function called my_suite()
def my_suite():
    # Toggle a decision variable
    need_input = True
    # Iterate while decision is True
    while need_input:
        # Create a variable to store menu() function
        selected_option = menu()
        # Create a list to store options in the menu
        options = ['c', 't', 'e', 'r', 'q']
        # Check if user choice is in the menu list
        if not selected_option.isalpha() or selected_option not in options:
            print("Invalid option. Please enter a valid option from the menu.")
            continue
        # Check each choice from the list
        # Check for option 'c'
        elif selected_option == "c":
            suite = unittest.TestSuite()
            suite.addTest(TestCaseZulkifli('test_area_circle_positive_values'))
            suite.addTest(TestCaseZulkifli('test_area_circle_negative_values'))
            suite.addTest(TestCaseZulkifli('test_area_circle_misc_values'))
            runner = unittest.TextTestRunner()
            print(runner.run(suite))
            continue
        # Check for option "t"
        elif selected_option == "t":
            suite = unittest.TestSuite()
            suite.addTest(TestCaseZulkifli('test_area_trapezium_positive_values'))
            suite.addTest(TestCaseZulkifli('test_area_trapezium_negative_values'))
            suite.addTest(TestCaseZulkifli('test_area_trapezium_misc_values'))
            runner = unittest.TextTestRunner()
            print(runner.run(suite))
            continue
        # Check for option "e"
        elif selected_option == "e":
            suite = unittest.TestSuite()
            suite.addTest(TestCaseZulkifli('test_area_ellipse_positive_values'))
            suite.addTest(TestCaseZulkifli('test_area_ellipse_negative_values'))
            suite.addTest(TestCaseZulkifli('test_area_ellipse_misc_values'))
            runner = unittest.TextTestRunner()
            print(runner.run(suite))
            continue
        # Check for option "r"
        elif selected_option == "r":
            suite = unittest.TestSuite()
            suite.addTest(TestCaseZulkifli('test_area_rhombus_positive_values'))
            suite.addTest(TestCaseZulkifli('test_area_rhombus_negative_values'))
            suite.addTest(TestCaseZulkifli('test_area_rhombus_misc_values'))
            runner = unittest.TextTestRunner()
            print(runner.run(suite))
            continue
        elif selected_option == "q":
            print("Thanks for using this Test Software :), Goodbye !")
            break


# Run test software by calling suite function
my_suite()
