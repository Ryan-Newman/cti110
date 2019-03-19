# CTI-110
# P4T1b: Initials
# Ryan Newman
# 01MAR2019

import turtle
import random

# setup the window with a background color
wn = turtle.Screen()
wn.bgcolor("black")

# assign a name to your turtle
donatello = turtle.Turtle()
donatello.speed(9)

# create a list of colours
sfcolor = ["white", "grey"]

# create a function to create different size snowflakes
def snowflake(size):

# move the pen into starting position
    donatello.penup()
    donatello.forward(10*size)
    donatello.left(45)
    donatello.pendown()
    donatello.color("white")

    # draw branch 8 times to make a snowflake
    N = random.randint(4, 8)
    for i in range(8):
        branch(size)
        if N == 8:
            donatello.left(45)
        else:
            donatello.left(30)

# create one branch of the snowflake
N = random.randint(2, 5)
def branch(size):
    for i in range(3):
        for i in range(3):
            donatello.forward(10.0*size/3)
            donatello.backward(10.0*size/3)
            donatello.right(45)
        donatello.left(90)
        donatello.backward(10.0*size/3)
        donatello.left(45)
    donatello.right(90)
    donatello.forward(10.0*size)

    # loop to create random different sized snowflakes with different starting co-ordinates

for i in range(N):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    sf_size = random.randint(1, 4)
    donatello.penup()
    donatello.goto(x, y)
    donatello.pendown()
    snowflake(sf_size)

# leave the window open until you click to close 
wn.exitonclick()  
