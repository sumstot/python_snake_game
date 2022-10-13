from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('data.txt') as f:
            h_score = int(f.read())
        self.score = 0
        self.high_score = h_score
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        with open('data.txt') as f:
            h_score = int(f.read())
        if self.score > self.high_score:
            with open('data.txt', mode='w') as file:
                file.write(str(self.score))
                self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
