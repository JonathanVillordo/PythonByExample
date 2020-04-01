#064 Draw a five-pointed star.
import turtle

def star():

    turtle.shape("turtle")

    for i in range(0,1):
        turtle.forward(200)
        for i in range(0,1):
            turtle.right(140)
            turtle.forward(200)
            turtle.right(140)
            turtle.forward(200)
            turtle.right(140)
            turtle.forward(200)
            turtle.right(151)
            turtle.forward(200)

    turtle.exitonclick()

star()
