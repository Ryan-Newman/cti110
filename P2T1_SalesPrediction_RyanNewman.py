# Sales Prediction
# 10FEB2019
# CTI-110 P2T1 - Sales Prediction
# Ryan Newman
#

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: $'))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * .23

# Displaly the profit
# Change the format to add comma's after every 3 digits
# format to 2 digit floating point
print('The profit is $', format(profit, ',.2f'))

# Allow the user to view the last results and end the program
input("Press any key to exit: ")
