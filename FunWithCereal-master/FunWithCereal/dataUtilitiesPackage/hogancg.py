# hogancg.py

# Name: Cameron Hogan
# email: hogancg@mail.uc.edu
# Assignment number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief description of the assignment: collaboration assignment demonstrating if everyone can follow directions from the TA
# Brief Description of what this module does: this module function to print fact from the cereal file
# Citations: Joseph Rainford
# Anything else that's relevant: as of doing this no

from csvUtilitiesPackage.csvUtilities import *

def hogancg():
    '''
    this function calls readCSV and prints out a fun fact about my cereal
    @param: none
    '''
    
    cerealInfo = readCSV()
    print ("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy")
    
if __name__ == "__main__":
    hogancg()