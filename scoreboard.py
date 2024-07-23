from turtle import Turtle
FONT = ('Courier', 40, 'normal')
ALIGN = 'center'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.display_scoreboard()

    def display_scoreboard(self):
        self.clear()
        self.write(arg=f'{self.score1} - {self.score2}', font=FONT, align=ALIGN)

    def left_scored(self):
        self.score1 += 1
        self.display_scoreboard()

    def right_scored(self):
        self.score2 += 1
        self.display_scoreboard()

    def game_over(self):
        self.clear()
        self.display_scoreboard()
        self.goto(0, 0)
        self.write('GAME OVER', font=FONT, align=ALIGN)