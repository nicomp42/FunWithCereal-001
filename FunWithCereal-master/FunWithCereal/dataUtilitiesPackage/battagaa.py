# Name: Alyssa Battaglia
# email: battagaa@mail.uc.edu
# Assignment Number: Fun with Cereal
# Due Date: 03/26/2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Class project using Github collaboration

# battagaa.py

#from csvUtilitiesPackage.csvUtilities import *


import csv

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


def battagaa():
    '''
    This function calls readCSV and prints out a fun fact about my cereal 
    @param None: 
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is:", cerealInfo[0][0], "and is very yummy.")
    
if __name__ == "__main__":
    battagaa()