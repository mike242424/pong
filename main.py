import turtle as t
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

paddle_one = Paddle((350, 0))
paddle_two = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=paddle_one.move_down, key='Down')
screen.onkey(fun=paddle_one.move_up, key='Up')
screen.onkey(fun=paddle_two.move_down, key='s')
screen.onkey(fun=paddle_two.move_up, key='w')

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_one) < 50 and ball.xcor() > 320 or ball.distance(paddle_two) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_scored()

    if ball.xcor() < -395:
        ball.reset_position()
        scoreboard.right_scored()

    if scoreboard.score1 >= 10 or scoreboard.score2 > 10:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
