#halbakjc
#Name: Josh Halbakken
# email: halbakjc@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024 
# Course/Section: IS-4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: reads a fun fact about my favorite cereal

# Brief Description of what this module does: reads a fun fact about my favorite cereal
# Citations: Joe Rainford
# Anything else that's relevant: N/A

from csvUtilitiesPackage.csvUtilities import *

def halbakjc():
    '''
    This function calls readCSV and prints out a fun fact abou my cereal
    @param none
    @return a sentence with my favorite cereal
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "it is very yummy")
if __name__ == "__main__":
    halbakjc()
