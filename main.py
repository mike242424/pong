import turtle as t
from paddle import Paddle

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

paddle_one = Paddle()
paddle_one.goto(350, 0)
paddle_two = Paddle()
paddle_two.goto(-350, 0)


screen.listen()
screen.onkey(fun=paddle_one.move_down, key='Down')
screen.onkey(fun=paddle_one.move_up, key='Up')
screen.onkey(fun=paddle_two.move_down, key='s')
screen.onkey(fun=paddle_two.move_up, key='w')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
