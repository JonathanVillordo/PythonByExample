#060 Draw a square.
import turtle

def square():

    turtle.shape('turtle')

    for i in range(0,4):
        turtle.forward(100)
        turtle.right(90)
    
    turtle.exitonclick()

square()
