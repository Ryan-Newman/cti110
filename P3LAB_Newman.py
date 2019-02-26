# CTI-110
# P3TLAB: Debugging
# Ryan Newman
# 26FEB2019
#
# This program takes a number grade and outputs a letter grade.
# This program will ask the user to input the numerical grade
# and display the corresponding letter grade.

# Establish the main class
def main():

# System uses 10-point grading scale
# Define each grade
    
    A_score = 90
    B_score = 80 
    C_score = 70 
    D_score = 60 
    # Declare score and get input from user
    score = int(input('Enter grade: '))

    # Create if, else, and elif statements to categorize grade
    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
            print('Your grade is: B')
    elif score >= C_score:
            print('Your grade is: C')
    elif score >= D_score:
            print('Your grade is: D')
    else:
        print('Your grade is: F')
   
# program start
main()
