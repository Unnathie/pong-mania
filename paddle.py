from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,posit,color_choice):
        super().__init__()
        self.posit=posit
        self.shape("square")
        self.goto(posit)
        self.color(color_choice)
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        y=self.ycor()+20
        self.goto(self.xcor(),y)
    def down(self):

        y = self.ycor() - 20
        self.goto(self.xcor(), y)










