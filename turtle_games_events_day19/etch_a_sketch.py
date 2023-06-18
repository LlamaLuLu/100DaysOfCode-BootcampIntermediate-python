# 17/6/2023

import turtle
from turtle import Turtle, Screen

tumnus = Turtle()
tumnus.speed("fastest")
screen = Screen()

# TODO: w = forward
# TODO: s = backwards
# TODO: a = counter-clockwise (left)
# TODO: d = clockwise (right)
# TODO: c = clear drawing

def move_forward():
    tumnus.forward(10)

def move_backward():
    tumnus.backward(10)

def turn_right():
    new_heading = tumnus.heading() - 15
    tumnus.setheading(new_heading)

def turn_left():
    new_heading = tumnus.heading() + 15
    tumnus.setheading(new_heading)

def clear_drawing():
    tumnus.clear()
    tumnus.penup()
    tumnus.home()
    tumnus.pendown()

screen.listen()
screen.onkey(move_forward, "w")  # no brackets when passing func
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear_drawing, "c")

screen.exitonclick()

