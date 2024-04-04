#main.py
# Name: Smita Magar
# email:diswamsa@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:04/11/2024
# Course/Section:IS 4010/001
# Semester/Year:spring/2024
# Brief Description of the assignment: this assignment is about collaborating with Git hub
# Brief Description of what this module does: define function to print fun fact about cereal 
# Citations:
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def diswamsa():
    '''
    This function calls read CSV and prints out a fun fact about my cereal
    @param none:

    '''
    cerealInfo = readCSV()
    print("my favorite cereal type is", cerealInfo[0][0], "and it is very yummy")
    
if __name__ == "__main__": 
    diswamsa()
