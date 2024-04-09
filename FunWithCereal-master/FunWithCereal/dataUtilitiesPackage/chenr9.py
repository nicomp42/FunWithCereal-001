#Name:Ruolin Chen
#email:chenr9@mail.uc.edu
#Assignment Title: Assignment 10
#Course: IS 4010
#Semester/Year: Spring 2024
#Brief Description: This module contains a function that generates an interesting about the cereal data
#Citations:
#Anything else that's relevant: 

#I added the read_csv function to get it to work as I had the same error as Mac users
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

def chenr9():
    '''
    this function calls readCSV and prints out a fun fact about my cereal
    @sparam none:
    '''
    
    cerealInfo = readCSV()
    print("My favorite cereal type is:", cerealInfo[0][0], "Puffed Wheat.")


if __name__ == "__main__":
    chenr9()
   