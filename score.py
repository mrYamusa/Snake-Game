from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def addscore(self):
        self.clear()
        self.score += 1
        self.updatescore()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGNMENT, font=("Courier", 30, "bold"))