# yemanert.py

# Name: Rhodas Yemaneab
# email: yemanert@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: 4/11/24
# Course/Section: IS4010 001
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaboration assignment demonstrating 31 students working together (some not here).
# Brief Description of what this module does. Do not copy/paste from a previous assignment. This module runs a functions that prints an interesting fact about the cereal data. 
# Citations: Joseph Rainford
# Anything else that's relevant: 


#I added this part because I'm using a mac.
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

def yemanert():
    '''
    This function calls readCSV and prints out a fun fact about my cereal.
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    yemanert()