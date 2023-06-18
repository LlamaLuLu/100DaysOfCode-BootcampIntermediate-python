# 13/6/2023

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

# TODO: 4. random walk
directions = [0, 90, 180, 270]
timmy.speed("fastest")
for i in range(100):
    timmy.color(random_color())
    timmy.pensize(10)
    timmy.forward(20)
    timmy.right(random.choice(directions))

screen = Screen()
screen.exitonclick()
