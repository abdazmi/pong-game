from turtle import Screen
from peddle import Peddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=1000,height=700)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)

l_peddle = Peddle(-470)
r_peddle = Peddle(470)
screen.listen()
screen.update()
screen.onkey(key="Up", fun= r_peddle.move_up1)
screen.onkey(key="Down", fun=r_peddle.move_down1)

screen.onkey(key="w", fun= l_peddle.move_up)
screen.onkey(key="s", fun=l_peddle.move_down)

ball = Ball()
score = Score()

game_is_on = True
time_lapse = 0.05
while game_is_on:
    time.sleep(time_lapse)
    ball.move_randomly()
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()

    if ball.xcor() > 440 and ball.distance(r_peddle) < 50 or ball.xcor() < -440 and ball.distance(l_peddle) < 50:
        ball.return_back()
        if time_lapse > 0.005:
            time_lapse -= 0.005


    if ball.xcor() > 500:
        score.l_goal()
        time.sleep(2)
        ball.move_otherSide()
        time_lapse = 0.05

    elif ball.xcor() < -500 :
        score.r_goal()
        time.sleep(2)
        ball.move_otherSide()
        time_lapse = 0.05

    screen.update()

screen.exitonclick()