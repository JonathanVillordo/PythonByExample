#068 Draw a pattern that will change each time the program is run.
#Use the random function to pick the number of lines, the length of each line and the angle of each turn.

import turtle
import random

lines = random.randint(5,20)

for x in range(0,lines):
    length = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()

