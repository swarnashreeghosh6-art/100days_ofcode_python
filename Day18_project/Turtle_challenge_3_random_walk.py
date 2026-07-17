import turtle
from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("turtle")
timmy.color("PaleVioletRed4")
timmy.width(10)
timmy.speed(6)
turtle.colormode(255)
def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour=(r,g,b)
    timmy.pencolor(colour)

angles=[0,90,180,270]
for i in range(50):
    change_color()
    angle = random.choice(angles)
    timmy.setheading(angle)
    timmy.forward(30)



screen=Screen()
screen.exitonclick()
