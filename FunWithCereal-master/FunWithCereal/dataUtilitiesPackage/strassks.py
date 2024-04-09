# Name: Kaileb Strasser
# email: strassks@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/4/2024
# Course/Section: IS-4010
# Semester/Year: Spring 2024
# Brief Description of the assignment: collaboration assignment demonstrating 30 people working together

# Brief Description of what this module does. Defines function to print fact from cereal file
# Citations: Joseph Rainford
# Anything else that's relevant: N/A
from csvUtilitiesPackage.csvUtilities import *
def strassks():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("my favorite cereal type is ", cerealInfo[0][0], "it is very yummy.")
    
if __name__ == "__main__":
    strassks()