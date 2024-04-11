#piperec.py
# Name: Elizabeth Piper    
# email: piperec@mail.uc.edu
# Assignment Number: FunWithCereal
# Due Date: 4/11/2024
# Course/Section: IS 4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaborate with the class to print interesting statements about CSV file.
# Brief Description of what this module does: In this module we created a function to read a CSV file and print a fun fact about the data. 
# Citations: Joseph Rainford
# Anything else that's relevant:

from csvUtilitiesPackage.csvUtilities import *

def piperec():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param: None
    @return: None
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[5][0], "and it is very yummy.")
    
if __name__ == "__main__":
    piperec()
    
    