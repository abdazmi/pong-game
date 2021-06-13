from turtle import Turtle

class Peddle(Turtle):
    def __init__(self, postion):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(x= postion, y=0)


    def move_up(self):
        y = self.ycor()
        y += 30
        x = self.xcor()
        self.goto(x= x, y= y)

    def move_up1(self):
        y = self.ycor()
        y += 50
        x = self.xcor()
        self.goto(x= x, y= y)

    def move_down(self):
        y = self.ycor()
        y -= 30
        x = self.xcor()
        self.goto(x=x, y=y)

    def move_down1(self):
        y = self.ycor()
        y -= 30
        x = self.xcor()
        self.goto(x=x, y=y)