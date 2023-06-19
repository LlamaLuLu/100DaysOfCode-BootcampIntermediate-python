from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):

    def __init__(self, co_ords):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(co_ords)
        self.setheading(90)

    def move_up(self):
        self.goto(self.xcor(), self.ycor()+20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor()-20)
