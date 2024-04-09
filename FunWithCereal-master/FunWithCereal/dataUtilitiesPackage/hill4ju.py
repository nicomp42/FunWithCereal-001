#hill4ju
# Name: JaJuan Hill
# email: Hill4ju@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2023
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: GitHub collaboration assignment

# Brief Description of what this module does: This module defines a function and runs it.
# Citations:
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def hill4ju():
    cerealInfo = readCSV()
    print("My favorite cereal type is:", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ =="__main__":
    hill4ju()
    