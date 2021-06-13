from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score = 0
        self.penup()
        self.goto(x=0,y=300)
        self.hideturtle()
        self.color("yellow")
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("arial", 20, "normal"))

    def l_goal(self):
        self.clear()
        self.l_score += 1
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("arial", 20, "normal"))

    def r_goal(self):
        self.clear()
        self.r_score += 1
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("arial", 20, "normal"))