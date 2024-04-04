# marti6aj.py
# Name: Andrew Martin
# email: marti6aj@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 11, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Create  a function that returns a string with an interesting and gramatically correct sentence about the cereal data.

# Brief Discription of what this module does:
# Citations: Mr. Joseph Rainford
# Anything else that's relevant


from csvUtilitiesPackage.csvUtilities import *

def marti6aj():
    '''
    This function calls readCSV and prints our a fun fact about my ceral
    @param none:
    @return: A sentence with my favorite cereal
    '''
    ceralData = readCSV()
    print("My favorite cereal type is", ceralData[4][0], "and it is very yummy!")

if __name__ == "__main__":
    marti6aj()