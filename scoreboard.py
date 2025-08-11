from turtle import Turtle
ALIGN="center"
FONT=("Rockwell Extra Bold",30,"normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(20,200)
        self.color("white")
        self.score1=0
        self.score2=0
        self.score()
    def score(self):
        self.write(arg=f"PLAYER-1  [{self.score1}]         PLAYER-2  [{self.score2}] ",align=ALIGN,font=FONT)
    def increase_p1(self):
        self.score1+=1
        self.clear()
        self.score()
    def increase_p2(self):
        self.score2+=1
        self.clear()
        self.score()

