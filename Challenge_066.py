# 066 Draw an octagon that uses a different colour (randomly selected from a list of six possible colours) for each line.
import turtle
import random

colors = ['red','green','gray','blue','yellow']

for i in range(0,8):
    turtle.color(random.choice(colors))
    turtle.forward(50)
    turtle.right(45)

turtle.exitonclick()
