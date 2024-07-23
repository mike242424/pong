import turtle as t


class PaddleOne(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.speed('fastest')
        self.setheading(90)
        self.goto(-350, 0)
        self.showturtle()

    def move_up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor(), y=new_y_position)

    def move_down(self):
        new_y_position = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y_position)
