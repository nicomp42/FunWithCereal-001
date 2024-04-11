#moorheaa.py

# Name: Anna Moorhead
# email:moorheaa@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 11, 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaboration assignment demonstrating 30 people working together
# Citations: Joseph Rainford
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def moorheaa():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none: 
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "it is very yummy.")
    
if __name__ == "__main__":
    moorheaa()
    

    
