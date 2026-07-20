import turtle
from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=500)
user_bet=screen.textinput(title="Make your bet",prompt="Who do u think will win?").lower()
colours=["red","blue","yellow","green","orange","purple"]
names=["Tim","Tom","Jake","Blake","Viv","Carson"]
all_turtles={}
for name in names:
    all_turtles[name]=Turtle(shape="turtle")
print(all_turtles)

y=100
for t,colour in zip(all_turtles.values(),colours):
    t.color(colour)
    t.penup()
    t.goto(x=-230, y=y)
    y-=40


race_on=True
while race_on:
    for turtle in all_turtles.values():
        if turtle.xcor() > 230:
            race_on = False
            winning_colour=turtle.pencolor()
            if winning_colour==user_bet:
                print("You have won!!")
            else:
                print(f"You have lost!{winning_colour.title()} turtle is the winner!")
        step=random.randint(0,10)
        turtle.forward(step)



































screen.exitonclick()