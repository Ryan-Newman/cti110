# CTI-110 - Nested Loops: This program calls for nested loops to create a shape. I chose 6 point star.
# P4HW4 - Nested Loops
# Ryan Newman
# 12MAR2019

import turtle   # Allows the use of turtles

# This program uses "turtle" to draw a 6 point star shape
# This program will use nested for loops in order to use one turtle to
# draw the 6 point star

# Establish the main class
def main():
 wn = turtle.Screen()      # Creates a playground for turtles
 wn.bgcolor("black")
 
 leonardo = turtle.Turtle()     # Create a turtle, assign to leonardo
 leonardo.color("blue")         # Change leonardo's color to blue
 leonardo.pensize(4)             # Change leonardo's size to 4

 l = 1
 for l in range(6):
     for l in range(1):                     # Start the for loop, have it iterate 5 times in order to draw the five points in the star
        leonardo.forward(50)        # Tell leonardo to move forward 50 units
        leonardo.left(150)               # Tell leaonardo to rotate left by 150 units
        leonardo.forward(50)        # Tell leonardo to move forward 50 units
        leonardo.right(90)            # Tell leonardo to rotate right 90 units, in order to become more precise
    
 wn.mainloop()                        # Wait for user to close window
 
# program start
main()
