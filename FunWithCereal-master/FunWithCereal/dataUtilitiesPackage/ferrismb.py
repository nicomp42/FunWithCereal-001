#ferrismb.py

# Name: Morgan Ferris
# email: ferrismb@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/2024
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: In this assignment the class collaborated to clone and push a cereal assignment.

# Brief Description of what this module does. Defines function to print fact from cereal file
# Citations: Joseph Rainford


from csvUtilitiesPackage.csvUtilities import *
def ferrismb():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("My favorite cereal tyoe is", cerealInfo[0][0], "and it is so delicious!")
    
if __name__ == "__main__":
    ferrismb()