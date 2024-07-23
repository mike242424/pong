import turtle as t


class PaddleTwo(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(1, 5)
        self.speed('fastest')
        self.setheading(90)
        self.goto(350, 0)
        self.showturtle()

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
