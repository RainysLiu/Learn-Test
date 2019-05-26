
import turtle
import time


turtle.pencolor("red")
turtle.fillcolor("red")



turtle.begin_fill()


turtle.forward(800)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.end_fill()


turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.right(-90)



turtle.pencolor("yellow")
turtle.fillcolor("yellow")



turtle.begin_fill()

for _ in range(5):
    turtle.forward(300)
    turtle.right(144)
turtle.end_fill()
time.sleep(1)

# turtle.penup()
#turtle.color('black')
turtle.done()
