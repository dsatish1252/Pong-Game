from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from line import Line
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG-GAME")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
line = Line()
score = Score()
ball = Ball()
screen.listen()
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)
screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)


flag = True
while flag:
    time.sleep(ball.mv_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # detecting if ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_ball()
        score.ls += 1
        score.update_score()
    if ball.xcor() < -380:
        ball.reset_ball()
        score.rs += 1
        score.update_score()
screen.exitonclick()
