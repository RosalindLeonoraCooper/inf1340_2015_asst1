#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("Error")


name_that_shape()

#!/usr/bin/env python
# I am ignoring everything above this line
# this was written and tested in Python 3. I still need to change input to raw_input.
shape = int(input("Please enter the number of sides of your polygon: "))
if shape < 3 or shape > 10:
    print("Error")
elif shape == 3:
    print("your polygon is a triangle")
elif shape == 4:
    print("a square!")
elif shape == 5:
    print("pentagon")
elif shape == 6:
    print("hexagonn")
elif shape == 7:
    print("heptagon")
elif shape == 8:
    print("octagon")
elif shape == 9:
    print("nonagon")
elif shape == 10:
    print("decagon")
