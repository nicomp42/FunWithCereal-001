#from csvUtilitiesPackage.csvUtilities import *
# Name: Joseph Rainford
# email: rainfojp@mail.uc.edu
# Assignment Number: Fun with Cereal Assignment 10
# Due Date: April 11, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment reads a CSV and prints out an interesting fact and is a large group project.

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this: This module is unique per student and has our own function.
# Citations: NA
# Anything else that's relevant: NA
import csv

# I did this because I am on a mac, and it was the only way it would work
def readCSV():
    """
    Read the cereals CSV file into a list of lists
    @return: The list of lists
    """
    with open('..\dataPackage\\cereals.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        cereals = []
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                cereals.append(row)
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        #print(cereals)
    return cereals

def rainfojp():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param none;
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is:", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    rainfojp()