# 14/6/2023

import turtle

from turtle import Turtle, Screen
import random
import colorgram

# colors_rgb = []
# palette = colorgram.extract("image.jpg", 30)
# for color in palette:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     n_color = (r, g, b)
#     colors_rgb.append(n_color)

colors_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
turtle.colormode(255)  # change to rgb colors
# TODO: 1. 10 x 10
# TODO: 2. radius = 20, space = 50

tumnus = Turtle()
tumnus.shape("classic")

tumnus.penup()
tumnus.hideturtle()
tumnus.speed("fastest")

tumnus.setheading(225)  # changes angle
tumnus.forward(310)
tumnus.setheading(0)

for row in range(10):
    for dot in range(10):
        tumnus.dot(20, random.choice(colors_list))
        tumnus.forward(50)
    tumnus.left(90)
    tumnus.forward(50)
    tumnus.right(90)
    tumnus.backward(500)


screen = Screen()
print(screen.canvheight)  #300
print(screen.canvwidth)  #400

screen.exitonclick()
