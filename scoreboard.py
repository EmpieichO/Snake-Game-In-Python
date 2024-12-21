from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.penup()
        self.color("blue")
        self.write(f"Score = {self.score}",False, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.score_update()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", False, align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 24, "normal"))
        self.score += 1
