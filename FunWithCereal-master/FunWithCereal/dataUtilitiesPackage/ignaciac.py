# ignaciac.py

# Name: Aimee Madrigal
# email: ignaciac@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date: April 11, 2024
# Course/Section: IS 4010 (001)
# Semester/Year: Spring 2024
# Brief Description of the assignment: 
# Brief Description of what this module does. This functions calls readCSV and prints outs a fun fact about my favorite cereal.
# Citations: Joseph Rainford
# Anything else that's relevant: N/A



# from csvUtilitiesPackage.csvUtilities import *
import csv 


# I did this because I'm on a Mac.

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

def ignaciac():
    '''
    This functions calls readCSV and prints outs a fun fact about my cereal
    @param none:
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is", cerealInfo[0][0], "it is very yummy.")
    
if __name__ == "__main__":
    ignaciac()
    
    
    
    
    