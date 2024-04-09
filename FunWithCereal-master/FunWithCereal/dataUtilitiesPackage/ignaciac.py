# ignaciac.py

# Name: Aimee Madrigal
# email: ignaciac@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 11, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: 
# Brief Description of what this module does. This functions calls readCSV and prints outs a fun fact about my favorite cereal.
# Citations: Joseph Rainford
# Anything else that's relevant: N/A




from csvUtilitiesPackage.csvUtilities import *

def ignaciac():
    '''
    This functions calls readCSV and prints outs a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "it is very yummy.")
    
if __name__ == "__main__":
    ignaciac()
    
    
    
    
    