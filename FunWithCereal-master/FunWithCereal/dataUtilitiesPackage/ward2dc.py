#ward2dc.py
#name:Duncan Ward
#email: ward2dc@mail.uc.edu
#assignment Number: Fun with Cereal
#Due date: March26, 2024
#course/section: IS4010-001
#semester/year: spring 2024
#Brief description: CLass project using Github collaboration 


#from csvUtilitiesPackage.csvUtilities import *
import csv

#I did this because i am on a mac and it is the only way it would work 

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

def ward2dc():
    '''
    this function calls readCSV and prints out a fun fact about my cereal
    @param: none
    '''
    cerealInfo = readCSV()
    print("my favorite cereal type is: ", cerealInfo[0][0], "and it is very yummy.")
    
if __name__ == "__main__":
    ward2dc()
    