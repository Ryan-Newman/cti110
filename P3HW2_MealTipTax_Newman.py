# CTI-110
# P3HW2 - MealTipTax
# Ryan Newman
# 25FEB2019
#
# Create a program that calculates the tip of the user's meal.
# The program will ask the user to choose the desired tip percentage.
# Display an error if the user enters an incorrect input
# With a correct input, calculate the tip and 7% sales tax
# Display all of the items: Tip, Tax, and Total

# Establish the variables for meal price, tip, tax, and total
# Get the Total meal price input from the user
meal_price = float(input('Total cost of the meal: $'))
tip = float(input('Would you like to leave 15%, 18%, or 20% tip: '))
tax = meal_price * .07
total = tax + meal_price + tip

# Create a variable for 15 percent tip
fifteen = meal_price * .15

# Create a variable for 18 percent tip
eighteen = meal_price * .18

# Create a variable for 20 percent tip
twenty = meal_price * .2

# Create the if statement for the tip options with a failsafe for other choices
if tip == 15:
    print("A tip of 15% = $", format(fifteen, ",.2f"))
elif tip == 18:
        print("A tip of 18% = $", format(eighteen, ",.2f"))
elif tip == 20:
            print("A tip of 20% = $", format(twenty, ",.2f"))
else :
    total = tax + meal_price
    print('Error: the value entered is not an option, tip is now 0%')

# Display the tax and the total on seperate lines
print("Your tax is $", format(tax, ",.2f"))
print("Your total is $", format(total, ",.2f"))
