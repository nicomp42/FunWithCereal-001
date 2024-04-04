# huntt3.py
#*********************************************************************************************************
# Names: Trevor Hunt                                                                                     *
# emails: huntt3@mail.uc.edu                                                                             *
# Assignment Number: Assignment 10                                                                       *
# Due Date: 04/11/2024                                                                                   *
# Course/Section: IS4010-001                                                                             *
# Semester/Year: Spring 2024                                                                             *
# Brief Description of the assignment: Collaboration assignment demonstrating 30 people working together *
#                                                                                                        *
# Brief Description of what this module does: Defines function to print fact from cereal file            *
# Citations:                                                                                             *
# Anything else that's relevant:                                                                         *
#*********************************************************************************************************

from csvUtilitiesPackage.csvUtilities import *

def huntt3():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none: 
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    huntt3()