from turtle import Screen, Turtle
from paddle import Paddle
from line import Line
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
line = Line((0, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()

    if ball.ycor()>290 or ball.ycor()<-290:
        ball.y_bounce()

    if ball.distance(r_paddle) < 63 and ball.xcor() == 330 or ball.distance(l_paddle) < 63 and ball.xcor() == -330:
        ball.x_bounce()

    if ball.xcor()>380:
        ball.reposition()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reposition()
        scoreboard.r_point()

screen.exitonclick()