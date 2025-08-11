from turtle import Turtle

class Design:
    def __init__(self):
        self.new_turtle_list = []
        self.create_dotted_line()

    def create_dotted_line(self):
        for y in range(-280, 300, 40):  # from bottom to top, every 40 pixels
            self.add_turtle((0, y))

    def add_turtle(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        new_turtle.goto(position)
        self.new_turtle_list.append(new_turtle)
