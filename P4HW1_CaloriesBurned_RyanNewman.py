# Calories Burned: Calculates the amount of calories burned in time intervals
# 10MAR2019
# CTI-110 P4HW1 - Calories Burned
# Ryan Newman
#

# This program keeps track of the calories burned over timed intervals
# with a rate of 5 cal per minute, with a loop that counts calories
# burned after 20, 35, and 45 minutes


# Establish the main class
def main():

    # Establish the minutes, calories, and total with formulas
    minutes = 0
        
    # Create the loop to increment the minutes and calories
    while minutes <= 45:
        minutes = minutes + 5
        calories =  minutes * 5
        # Create an if statement to display each of the calories burned
        if minutes == 20 or minutes == 35 or minutes == 45:
            print('you have burned ', calories, ' calories in ', minutes)
           
# program start
main()
