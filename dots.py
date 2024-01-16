from turtle import Turtle, Screen, colormode
import random

tinny = Turtle()
colormode(255)
tinny.speed("fastest")
tinny.hideturtle()
tinny.up()

y = -200 
x = -300
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
for j in range(10):
    tinny.setpos(x,y)
    tinny.down
    for i in range(10):
        tinny.dot(20,random_color())
        tinny.forward(50)
        y += 5
    

screen = Screen()

screen.exitonclick()