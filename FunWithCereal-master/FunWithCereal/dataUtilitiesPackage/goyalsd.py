#goyalsd.py
# Name: Sonali Goyal
# email: goyalsd@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/11/2024
# Course/Section: IS 4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaborating with the class on an assignment

# Brief Description of what this module does: Prints an interesting sentence about cereal
# Citations: Joseph Rainford - kudos to him
# Anything else that's relevant:  

from csvUtilitiesPackage.csvUtilities import *

def goyalsd():
    '''
    This function calls readCSV and prints out a fun fact about my cereal.
    @param: none
    @return: A sentence with my favorite cereal 
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is ", cerealInfo[0][0], "and it is very yummy.")

if __name__ == "__main__":
    goyalsd()
    