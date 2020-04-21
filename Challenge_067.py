#067Create the following pattern
import turtle

for i in range(0,10):
    turtle.right(35)
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    
turtle.exitonclick()
