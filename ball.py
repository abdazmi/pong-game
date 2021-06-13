from turtle import  Turtle
from random import Random
SPEED = 10

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self.y_mark = 1
        self.x_mark = 1
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.goto(0,0)

    def move_randomly(self):

        self.x += SPEED * self.x_mark
        self.y += SPEED * self.y_mark
        self.goto(x=self.x, y=self.y)

    def bounce(self):
        self.y_mark *= -1

    def return_back(self):
        self.x_mark *= -1

    def move_otherSide(self):
        self.home()
        self.x = 0
        self.y = 0
        self.y_mark *= -1
        self.x_mark *= -1
