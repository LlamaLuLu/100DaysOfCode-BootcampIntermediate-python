# 14/6/2023

from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
timmy.shape("turtle")

# colours = ["plum", "orange", "firebrick", "medium aquamarine",
# "cadet blue", "dark salmon", "saddle brown", "pale violet red"]

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors

# TODO: 5. draw spirograph
timmy.speed("fastest")
timmy.shape("classic")
for i in range(60):
    angle = 360 / 60
    timmy.color(random_color())
    timmy.circle(100)  # radius = 100
    timmy.left(angle)

screen = Screen()
screen.exitonclick()
