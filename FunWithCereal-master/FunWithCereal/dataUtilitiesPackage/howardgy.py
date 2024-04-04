#howardgy.py

# Name: Gillian Howard
# Email: howardgy@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: IS4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaborating assignment demonstrating 30 people working together

# Brief Description of what this module does: This module defines a function that reads the CSV file about cereal data and prints a statement
# Citations: Joseph Rainford
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def howardgy():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none
    @return: A sentence with my favorite cereal
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    howardgy()
    