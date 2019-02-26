# Get the area of Rectangles
# 21FEB2019
# CTI-110 P3T1 - Area of Rectangles
# Ryan Newman
#
# This program asks for the length and width of two rectangles.
# The program should tell the user which rectangle has the greater area,
# or if the two rectangles have equal area.

# Create a variables for the Width and Length of the first Rectangle
# Create the formula for the area of the first Rectangle, multiply W * L
Rectangle1W = float(input('Total Width of the first Rectangle: '))
Rectangle1L = float(input('Total Length of the first Rectangle: '))
Rectangle1A = Rectangle1L * Rectangle1W


# Create a variables for the Width and Length of the second Rectangle
# Create the formula for the area of the second Rectangle, multiply W * L
Rectangle2W = float(input('Total Width of the second Rectangle: '))
Rectangle2L = float(input('Total Length of the second Rectangle: '))
Rectangle2A = Rectangle2L * Rectangle2W

# Create a nested if statement that shows which of the Rectangles have
# a greater area or if both Rectangles have equal area.
if Rectangle1A > Rectangle2A:
    print("The Area of the first Rectangle is larger than the Area of the second")
else:
    if Rectangle1A < Rectangle2A:
        print("The Area of the second Rectangle is larger than the Area of the First")
    else:
        print("The Area of both Rectangles are the same")
