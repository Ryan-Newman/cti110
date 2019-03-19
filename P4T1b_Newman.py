# CTI-110
# P4T1b: Initials
# Ryan Newman
# 01MAR2019

import turtle   # Allows the use of turtles

# This program uses "turtle" to draw a my initials R N
# The program will have two turtles that will each draw a different letter

# Establish the main class
def main():
 wn = turtle.Screen()      # Creates a playground for turtles
 wn.bgcolor("yellow")       # Changes the backgrounds color to black
 
 r = turtle.Turtle()     # Create a turtle, assign to leonardo
 r.color("blue")         # Change leonardo's color to blue
 r.pensize(3)            # Change leonardo's size to 2
 
 n = turtle.Turtle()      # Create another turtle, assigned to raphael
 n.color("red")           # Change raphael's color to red
 n.pensize(3)             # Change raphael's size to 3

 r.left(90)       # r rotates 90 degrees
 r.forward(90)    # r goes up
 r.right(90)      # r rotates right 90 degrees
 r.forward(30)    # r moves forward 30 units
 r.right(90)
 r.forward(30)
 r.right(90)
 r.forward(30)
 r.right(230)
 r.forward(75)

 n.penup()        # Makes the drawing line invisible
 n.forward(60)    # n moves forward by 60 units
 n.pendown()      # makes the drawing line visible again
 n.left(90)       # n turns by 90 degrees
 n.forward(90)
 n.right(160)
 n.forward(95)
 n.left(160)
 n.forward(95)
 
 wn.mainloop()                  # Wait for user to close window
 
# program start
main()
