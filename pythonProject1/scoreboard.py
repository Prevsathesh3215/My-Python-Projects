from turtle import *
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self, x, y, player_num):
        super().__init__()
        self.color("white")
        self.pu()
        self.score = 0
        self.setpos((x, y))
        self.write(self.score, align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.play_num = player_num

    def add_one(self):
        self.clear()
        self.score += 1
        self.write(self.score, align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\nPLAYER {self.play_num} WINS!", align=ALIGNMENT, font=FONT)

    def game_over_draw(self):
        self.goto(0, 0)
        self.write("DRAW", align=ALIGNMENT, font=FONT)