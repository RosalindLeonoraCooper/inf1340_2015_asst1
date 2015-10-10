#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    print("The battery cables may be damaged. Replace cables and try again.")


diagnose_car()

#!/usr/bin/env python
# I am ignoring everything above this line.
# 1340 exercise 3, assignment 1
# trouble shooting car issue with expert system
# Written and tested in python 3. need to change input to raw_input
question1 = input("Is the car silent when you turn the key? (yes/no) ")
if question1 == 'yes':
    question1_1 = input("Are the battery terminals corroded? (yes/no) ")
    if question1_1 == 'yes':
        print("Clean the terminals and try starting again.")
    elif question1_1 == 'no':
        print("Replace cables and try again.")
elif question1 == 'no':
    question1_2 = input("Does the car make a clicking noise? (yes/no) ")
    if question1_2 == 'yes':
        print("Replace the battery.")
    elif question1_2 == 'no':
        question2 = input("Does the car crank up but fail to start? (yes/no) ")
        if question2 == 'yes':
            print("Check spark plug connections")
        elif question2 == 'no':
            question3 = input("Does the engine start and then die? (yes/no) ")
            if question3 == 'no':
                print("System has no response.")
            elif question3 == 'yes':
                question4 = input("Does your car have fuel injection? (yes/no) ")
                if question4 == 'no':
                    print("Check to ensure the choke is opening and closing.")
                elif question4 == 'yes':
                    print("Get it in for service.")

