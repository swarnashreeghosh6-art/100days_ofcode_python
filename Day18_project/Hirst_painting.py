import turtle
from turtle import Turtle,Screen
import random
timmy=Turtle()
timmy.shape("arrow")
timmy.hideturtle()
timmy.speed(0)
turtle.colormode(255)
timmy.up()
timmy.setpos(-200,-200)

colour_list=[(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20)]
def move_in_x_axis():
    for x in range(10):
        colour = random.choice(colour_list)
        timmy.dot(20, colour)
        timmy.forward(50)
for y in range(5):
    move_in_x_axis()
    for i in range(2):
        timmy.left(90)
        timmy.forward(50)
    move_in_x_axis()
    for j in range(2):
        timmy.right(90)
        timmy.forward(50)














screen=Screen()
screen.exitonclick()
