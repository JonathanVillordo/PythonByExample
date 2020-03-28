#061 Draw a triangle.

import turtle

def triangle():

    turtle.shape('turtle')
    
    for i in range(0,1):
        turtle.forward(100)
        for g in range(0,1):
            turtle.right(120)
            turtle.forward(100)
            turtle.right(120)
            turtle.forward(100)
    
    turtle.exitonclick()

triangle()
