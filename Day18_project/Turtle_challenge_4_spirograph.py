import turtle
from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("turtle")
timmy.color("PaleVioletRed4")
timmy.speed(0)
turtle.colormode(255)
def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour=(r,g,b)
    timmy.pencolor(colour)

def spirograph(tilt):
    no_of_times=int(360/tilt)
    for i in range(no_of_times):
        change_color()
        timmy.circle(80)
        timmy.setheading(timmy.heading() + tilt)

spirograph(5)


screen=Screen()
screen.exitonclick()
