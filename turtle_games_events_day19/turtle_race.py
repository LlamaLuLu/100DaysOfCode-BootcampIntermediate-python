# 17/6/2023

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)  # set screen size
user_guess = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter colour: ")

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_coords = [-80, -50, -20, 10, 40, 70]
all_turtles = []

for obj in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[obj])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coords[obj])  # turtle size: 40x40
    all_turtles.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour == user_guess:
                print(f"You've won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_colour} turtle is the winner!")
        distance = random.randint(0, 10)  # [0, 10]
        turtle.forward(distance)


screen.exitonclick()
