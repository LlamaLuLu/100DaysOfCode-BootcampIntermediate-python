# 13/6/2023

from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
timmy.shape("turtle")

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# TODO: 3. draws from triangle -> decagon
for shape in range(7):
    angle = 360 / (3 + shape)
    timmy.color(random_color())
    for side in range(3+shape):
        timmy.forward(100)
        timmy.right(angle)

screen = Screen()
screen.exitonclick()
