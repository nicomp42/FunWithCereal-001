'''
Created on Apr 9, 2024

@author: Carto
'''
#from csvUtilitiesPackage.csvUtilities import *
#from mainPackage.main import myCereals
from csvUtilitiesPackage.csvUtilities import *

def bowersas():
    '''
    this function calls readCSV and prints out a fun fact about myCereals
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is,", cerealInfo[0][0]," and it is very yummy")
    
if __name__ == "__main__":
    bowersas()