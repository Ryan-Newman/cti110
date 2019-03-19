# Pounds to Kilograms: displays a table of 100 - 300lbs with equivalent Kilograms
# 10MAR2019
# CTI-110 P4HW2 - Pounds to Kilograms
# Ryan Newman
#

# This program converts 100 to 300 pounds in increments of 10
# Into the equivalent in Kilograms. Kg = lb/2.2046 display the table using a for loop

# Establish the main class
def main():

    # Create the loop to increment the iterations of lbs in the table and establish kg formula
    # using a for loop establish 100 lbs, allow up to 310lbs to display 300 since 0 is a starting
    # count, and increment by 10

    for lbs in range(100, 310, 10):
              kg = lbs / 2.2046
              print(lbs, 'lbs is ', kg, 'kgs')   
           
# program start
main()
