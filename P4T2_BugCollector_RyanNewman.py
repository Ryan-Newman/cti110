# Bug collector: counts the number of bugs collected per day for 5 days
# 09MAR2019
# CTI-110 P4T2 - Bug Collector
# Ryan Newman
#

# This program keeps track of the running count total of bugs collected 
# for a period of 5 days. The program creates a loop that asks for the 
# number of bugs collected each day, after the loop, the total number of
# bugs collected is displayed

# Establish the main class
def main():

    # Establish the variable for the total
    total = 0

    # Get the bugs collected for each day using a for loop
    for day in range(1, 6):
        print('Enter the bugs collected on day', day, ':')
        bugs = int(input())
        total += bugs

    # Display the total bugs.
    print('You collected a total of ', total, 'bugs.')
       
   
# program start
main()
