# Name: Nosagie Sherman
# email: shermani@mail.uc.edu
# Assignment Number: FunWithCereal
# Due Date: 4/11/2024
# Course/Section:  IS 4030 - 002
# Semester/Year: Spring 2024
# Brief Description of the assignment: Collaborate with class to print interesting statments
# Citations: Joesph Rainford
# Anything else that's relevant: In this module we create a CSV file and say a fun fact about it 





import csv
#from csvUtilitiesPackage.csvUtilities import * 
#from FunWithCereal.csvUtilitiesPackage.csvUtilities import readCSV
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

def shermani():
    '''
    This function calls readCSV and prints out a fun fact about my cereal
    @param: none
    @return: none
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is ", cerealInfo[5][0], "and it was delicious.")
    
    
if __name__ == "__main__":
    shermani()