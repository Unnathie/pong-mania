from turtle import Turtle
import  random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("magenta")
        self.shape("circle")
        self.x_move=10
        self.y_move=10
        self.speeding_ball=0.1
    def move(self):
        self.right(90)
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)
    def switch_y(self):
        self.y_move*=-1
    def switch_x(self):
        self.x_move*=-1
        self.speeding_ball*=0.9
    def reset_position(self):
        self.goto(0,0)
        self.speeding_ball=0.1

