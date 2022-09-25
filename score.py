from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_board = 0
        with open("high_score.txt") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.write(f"Score: {self.score_board}  High Score: {self.high_score}", align="center",
                   font=("Aerial", 20, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.clear()
        self.score_board += 1
        self.write(f"Score: {self.score_board}  High Score: {self.high_score}", align="center",
                   font=("Aerial", 20, "normal"))

    def refresh(self):
        if self.score_board > self.high_score:
            self.high_score = self.score_board
            with open("high_score.txt", mode="w") as f:
                f.write(f"{self.high_score}")
            self.score_board = 0
        self.write(f"Score: {self.score_board}  High Score: {self.high_score}", align="center",
                   font=("Aerial", 20, "normal"))
