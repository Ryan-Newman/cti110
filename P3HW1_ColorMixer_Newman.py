# CTI-110
# P3HW1 - Color Mixer
# Ryan Newman
# 21FEB2019
#
# This program asks the user to enter the names of two primary colors to mix.
# If the user enters anything other than "red," "blue," or "yellow," the program
# should display an error message. Otherwise, the program should display the name
# of the secondary color that results.

# Ask the user to enter two primary colors
# Establish which colors are primary
# Create a failsafe for any input other than primary colors
print("Primary colors are red, yellow, and blue.")
primary1 = input('Enter primary color 1: ')
if primary1 == 'blue':
    primaryColor = True
elif primary1 == 'red':
    primaryColor = True
elif primary1 == 'yellow':
    primaryColor = True
else:
    primary1 != 'red''yellow''blue'   
    print("Error: This is not a primary color!")
    
# Repeat the primary1 steps for primary 2    
primary2 = input('Enter primary color 2: ')
if primary2 == 'blue':
    primaryColor = True
elif primary2 == 'red':
    primaryColor = True
elif primary2 == 'yellow':
    primaryColor = True
else :
    primary2 != 'blue''yellow''red'
    print("Error: This is not a primary color!")

#Establish the a message for the same color
if primary1 == primary2:
    print("You have chosen the same color, it will remain the same")

# Establish the combination for purple
if primary1 == 'blue' and primary2 == 'red' or primary1 == 'red' and primary2 == 'blue':
    print("The mixed color is purple.")

# Establish the combination for green
if primary1 == 'blue' and primary2 == 'yellow' or primary1 == 'yellow' and primary2 == 'blue':
    print("The mixed color is green.")

# Establish the combination for orange
if primary1 == 'red' and primary2 == 'yellow' or primary1 == 'yellow' and primary2 == 'Red':
    print("The mixed color is orange.")


