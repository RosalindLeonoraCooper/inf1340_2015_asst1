#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


money = 1000.00
print

# I am ignoring everything written above this line.
# INF1340, exercise one, assignment one. Fall, 2015.
# I have written three functions. They are written in Python 3 and have been tested in the
# python shell (IDLE)
# these functions are written in accordance with the method and style specified by the \
# "function design recipe" outlined in the Gries, Campbell, and Montojo textbook, 2nd ed.
# here is the first function
def price_of_shares(shares, unit_price):

    """ (num, num) num

    Returns price paid for n number of shares bought or sold at\
    unit_price.

    Here are two example calls which I tested in the Python 3.4.3 shell:

    price_of_shares(500, 40)
    20000

    price_of_shares(1000, 10)
    10000

    """

    return shares * unit_price

# here is the second function
def commission_on_price(price, commission):

    """ (num, num) num

    Returns the percent of commission paid on price.

    Here are two example calls, which I tested as above:

    commission_on_price(20000, 4)
    800.0

    commission_on_price(10000, 10)
    1000.0

    """

    return (commission * price) / 100

# here is the third function
def true_price_of_shares(price_of_shares, commission_on_price):

    """

    (num, num) num

    Returns the price_of_shares minus the commission_on_price.

    Here are two example calls, which I tested as above:

    true_price_of_shares(20000, 800)
    19200

    true_price_of_shares(10000, 1000)
    9000

    """

    return price_of_shares - commission_on_price

# I tried to write a function using the foregoing functions in order to\
# calculate gains and/or losses after stock transactions. But I ended up in\
# a bit of a muddle. Sorry.













