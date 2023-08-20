from turtle import Turtle

class Line(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('red')
        self.shape('square')
        self.shapesize(stretch_len=0.2, stretch_wid=50)
        self.penup()
        self.goto(position)

