# Name:Chase McClure
# email:mcclurc2@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: ADV APP DEV (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: collaboration assignment demonstrating if everyone can follow directions from the TA
# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this.  this module function to print fact from the cereal file
# Citations: Joseph Rainford
# Anything else that's relevant: as of doing this no





from csvUtilitiesPackage.csvUtilities import *

def mcclurc2():
    '''
    this function calls readCSV and prints out a fun fact about my cereal
    @param: none
    '''
   
    cerealInfo = readCSV()
    print ("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy")

if __name__ == "__main__":
    mcclurc2()