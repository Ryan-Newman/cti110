# Sum of Numbers: User enters positive numbers for a sum, negative numbers initiate the sum.
# 10MAR2019
# CTI-110 P4HW3 - Sum of numbers
# Ryan Newman
#

# This program uses a loop for the user to enter positive numbers to total a sum
# A negative number will initiate the calculation of all the positive numbers
# An if statement prevents the negative number from being calculated into the sum

def main():                                         # Establish the main class
    total = 0                                        # Initiate the total variable
    number = float(input('Please enter in a positive number. Enter a negative number to calculate sum: '))
    while number > 0:                         # Create a while loop to  activate for positive numbers
        total = total + number               # Assign the total to a formula
        number = float(input('Enter a positive number: '))
    if number < 0:                               # Use an if statement to stop the program for negative numbers, without calculating negative numbers
       print('The sum of your numbers is: ', total)

main()                                              # Start the program by calling main()
