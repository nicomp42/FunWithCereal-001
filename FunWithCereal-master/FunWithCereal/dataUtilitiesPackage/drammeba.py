# Name: Binta Drammeh
# Email: Drammeba@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 11th, 2024
# Course/Section: IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Write a function that as a class that returns an interesting statement about the cereal data
# Citations: Joeseph Rainford
# Anything else that's relevant:

#main.py

from csvUtilitiesPackage.csvUtilities import *

def drammeba():
    '''
    This function calls readcvs and prices out of a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "it is very yummy")

if __name__ == "__main__":   
    drammeba()
