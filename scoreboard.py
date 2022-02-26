import time
from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../Desktop/data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 260)
        self.clear()
        self.write(f"Score = {self.score}      "
                   f"High Score = {self.highscore}", False, align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}      "
                   f"High Score = {self.highscore}", False, align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("../../Desktop/data.txt", mode="w") as file:
                file.write(str(self.highscore))
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=("Arial", 35, "normal"))
        time.sleep(1)
        self.clear()
