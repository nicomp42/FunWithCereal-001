# csvUtilities
# Utility functions for processing the CSV files are defined here
# Bill Nicholson
# nicholdw@ucmail.uc.edu
# IS4010-001 Spring 2024
import csv

def readStudentIDs():
    """
    Read student IDs into a list
    @return: The list
    """
    return ["battagaa",
"bowersas",
"chenr9",
"drammeba",
"elmorejc",
"ferrismb",
"garreaa",
"goyalsd",
"halbakjc",
"hill4ju",
"hogancg",
"howardgy",
"huntt3",
"kinkadrj",
"laughlcd",
"ignaciac",
"diswamsa",
"marti6aj",
"mcclurc2",
"moorheaa",
"piperec",
"rainfojp",
"roopnacn",
"schillmx",
"shermani",
"strassks",
"teowramm",
"turne2jw",
"walsh2ct",
"ward2dc",
"yemanert"]


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