from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)
        self.update_screen()

    def update_screen(self):
        self.write(arg=f"Score :  {self.score}", align="center", font=("Courier", 14, "normal"))


    def add_score(self):
        self.score += 1
        self.clear()
        self.update_screen()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("Courier", 14, "normal"))


