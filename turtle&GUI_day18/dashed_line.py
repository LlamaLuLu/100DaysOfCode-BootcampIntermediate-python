# 13/6/2023

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

# TODO: 2. dashed line
for i in range(10):
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()
