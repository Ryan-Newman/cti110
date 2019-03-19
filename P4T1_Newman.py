# CTI-110
# P4T1: Turtle Graphics
# Ryan Newman
# 01MAR2019

import turtle   # Allows the use of turtles

# This program uses "turtle" to draw a square and a triangle
# The program will have two turtles that will each draw a different shape
# This program will use for loops to ensure no infinite loop is present
# For fun, the background will change at the end of the program

# Establish the main class
def main():
 wn = turtle.Screen()      # Creates a playground for turtles
 wn.bgcolor("black")
 
 leonardo = turtle.Turtle()     # Create a turtle, assign to leonardo
 leonardo.color("blue")         # Change leonardo's color to blue
 leonardo.pensize(2)            # Change leonardo's size to 2
 
 raphael = turtle.Turtle()      # Create another turtle, assigned to raphael
 raphael.color("red")           # Change raphael's color to red
 raphael.pensize(3)             # Change raphael's size to 3
  
 l = 1
 for l in range(4):
    leonardo.backward(90)       # Tell leonardo to move forward by 90 units
    leonardo.right(90)          # Tell leonardo to turn by 90 degrees
 for l in range(3):
        raphael.forward(200)    # Tell raphael to move forward by 200 units
        raphael.left(120)       # Tell raphael to turn by 120 degrees
 if l <= 4:                     # Create an if statement for the background change condition
     wn.bgcolor("white")        # Change the background color after the shapes are drawn

 wn.mainloop()                  # Wait for user to close window
 
# program start
main()
