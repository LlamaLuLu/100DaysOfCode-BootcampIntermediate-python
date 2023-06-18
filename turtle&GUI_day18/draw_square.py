# 13/6/2023

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")

# TODO: 1. draws square
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

screen = Screen()
screen.exitonclick()
