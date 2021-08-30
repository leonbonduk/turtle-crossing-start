from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-280, 250)
        self.hideturtle()
        self.level_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level_score += 1
        self.write("Level: " + str(self.level_score), align="left", font= ("Courier", 40, "normal"))

    def game_over(self):
        self.clear()
        self.write("Game Over", align="left", font= ("Courier", 40, "normal"))
