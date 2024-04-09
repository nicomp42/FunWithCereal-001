# Name: Cian Roopnarine
# email: roopnacn@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/11/24
# Course/Section: IS 4010
# Semester/Year: 2024 Spring
# Brief Description of the assignment: Work together as a class to pull and push a github project.

# Brief Description of what this module does. Creates a function and calls the data to create a string
# Citations: Joseph Rainford
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def roopnacn():
    cerealInfo = readCSV()
    print ("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    roopnacn()
