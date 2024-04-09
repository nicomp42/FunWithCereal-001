#main.py
# Name: Riley Kinkade
# email: kinkadrj@mail.uc.edu
# Assignment Number: Assignment10
# Due Date: 4/11/24
# Course/Section: Adv App Dev (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaboration Assigment
# Define function to print fact from cereal file
# Joe RainFord
from csvUtilitiesPackage.csvUtilities import *

def Kinkadrj():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none:
    @return: A sentence with my favorite cereal
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], " and it is yummy")
    
if __name__ == "__main__":
    Kinkadrj()