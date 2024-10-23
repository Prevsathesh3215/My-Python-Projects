from turtle import *
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.score = 0

        with open("my_file.txt", mode='r') as f:
            self.highscore = int(f.read())

        self.setpos((20, 240))
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def add_one(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("my_file.txt", mode='w') as f:
                f.write(str(self.highscore))

        self.score = 0
        self.write_score()


