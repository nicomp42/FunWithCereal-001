# walsh2ct.py
# Name: Connor Walsh
# email: walsh2ct@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/11/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: demonstrates use of modularity amongst large group of people

# Brief Description of what this module does. This module creates a function that prints a fact about cereal data.
# Citations:
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def walsh2ct():
    '''
    this function calls readCSV and prints out a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    walsh2ct()