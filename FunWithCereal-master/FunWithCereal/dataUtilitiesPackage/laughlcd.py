# Name: Connor Laughlin
# email: laughlcd@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 04/11/24
# Course/Section: IS4010 Section 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Forms a function that writes a random fun sentence about cereal.
# Brief Description of what this module does: Calls readCSV and prints out a fun sentence about cereal.
# Citations:
# Anything else that's relevant: Joseph Helped Me

# laughlcd.py

from csvUtilitiesPackage.csvUtilities import *

def laughlcd():
    '''
    This function calls readCSV and prints out a fun fact about cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("Rumor has it Joseph Rainford really loves", cerealInfo[0][0], "cereal.")
    
if __name__ == "__main__":
    laughlcd()
