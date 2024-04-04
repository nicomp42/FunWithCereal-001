# Name: Mikaela Teowratanakul
# email: teowramm@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: collaborate without errors and create a pull request on github with no conflicts
# Brief Description of what this module does: collaborated without errors and create a pull reqest on github with no conflicts
# Citations: Joseph Rainford
# Anything else that's relevant: N/A

from csvUtilitiesPackage.csvUtilities import *

def teowramm():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param: None
    '''
    cerealinfo = readCSV()
    print("My favorite cereal type is", cerealinfo[0][0], " and it is very yummy")
    
    
if __name__ == "__main__":
    teowramm()
     
     

