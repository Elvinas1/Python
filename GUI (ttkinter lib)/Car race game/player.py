from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.setheading(90)
        self.shapesize(3,3)
        self.penup()
        self.color('blue')
        self.goto(0,-200)

    def move_right(self):
        new_x = self.xcor() + 60
        self.goto(new_x,self.ycor())
    def move_left(self):
        new_x = self.xcor() - 60
        self.goto(new_x,self.ycor())