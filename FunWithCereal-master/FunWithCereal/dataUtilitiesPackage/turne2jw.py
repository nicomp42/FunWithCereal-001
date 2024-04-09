# Name: Jared Turner
# email: turne2jw@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:04/11/2024
# Course/Section: IS4010-001
# Semester/Year: spring 2024
# Brief Description of the assignment: gives you an interesting cereal fact
# Brief Description of what this module does. This module prints a unique statement
# Citations: class, and Joseph
# Anything else that's relevant:
from csvUtilitiesPackage.csvUtilities import *
def turne2jw():
    '''
    This function calls readCSV aand prints out a fun fact
    @param none
    @returns: A string with cereal 
    '''
    cerealInfo = readCSV()
    print("my favorite cereal is", cerealInfo[10][0], "it is very yummy")
if __name__ == "__main__":
    turne2jw()