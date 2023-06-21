from turtle import Turtle
import pandas
import random
COLORS = ["blue", "red"]

class State(Turtle):

    def __init__(self, guess):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color(random.choice(COLORS))
        self.state_name = guess
        self.goto(self.find_coords(guess))
        self.write(self.state_name, align="center", font=("Courier", 10, "normal"))

    def find_coords(self, guess):
        data = pandas.read_csv("50_states.csv")
        row = data[data.state == guess]
        x_pos = int(row.x.iloc[0])  # get int value
        y_pos = int(row.y.iloc[0])
        coords = (x_pos, y_pos)
        return coords
