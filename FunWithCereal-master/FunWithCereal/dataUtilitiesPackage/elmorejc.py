#elmorejc.py

# Name: Jake Elmore
# email: Elmorejc@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 11 2024
# Course/Section: IS 4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaboration assignment demonstrating 30 people working together
# Brief Description of what this module does: Defines function to print a fun fact
# Citations: Joe rainford
# Anything else that's relevant:


from csvUtilitiesPackage.csvUtilities import *

def elmorejc():
    '''
    This function call readsCSV and prints out a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[12][0], "and it tastes amazing")
    
if __name__=="__main__":
    elmorejc()
