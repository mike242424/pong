import turtle as t
from paddle_one import PaddleOne
from paddle_two import PaddleTwo

screen = t.Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

paddle_one = PaddleOne()
paddle_two = PaddleTwo()

screen.listen()
screen.onkey(fun=paddle_one.move_down, key='Down')
screen.onkey(fun=paddle_one.move_up, key='Up')
screen.onkey(fun=paddle_two.move_down, key='s')
screen.onkey(fun=paddle_two.move_up, key='w')

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
