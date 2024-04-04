#schillmx.py
# Name: Max Schiller
# Email: schillmx@mail.uc.edu
# Assignment: 10
# Due Date: April 11
# Course/Section: IS4010
# Semester/ Year: 2024
# Brief Description of the assignment: Collaboration assignment demonstrating
# Brief description of what this module does: Defines function to print fact from cereal file
# Citations: Joseph Rainford
# Anything else thats relevant: Shoutout Joseph






from csvUtilitiesPackage.csvUtilities import*
def schillmx():
    '''
    This function calls readCSV and prints out a fun fact about cereal
    @param none
    @return: a sentence with my favorite cereal
    '''
    cerealInfo = readCSV()
    print("My favorite cereal type is" , cerealInfo[0][0], "It is very yummy.")
    
if __name__ == "__main__":
    schillmx()
    