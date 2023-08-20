from turtle import Turtle


class Drawer(Turtle):
    def __init__(self):
        super().__init__()
        self.color('red')
        self.hideturtle()
        self.penup()
        self.goto(290,0)
        self.pendown()
        self.goto(290, 270)
        self.goto(-290, 270)
        self.goto(-290, -290)
        self.goto(290, -290)
        self.goto(290, 0)

