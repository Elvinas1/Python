from turtle import Turtle

class Drawroad(Turtle):
    def __init__(self):
        super().__init__()
        self.speed('fastest')
        self.pensize(3)
        self.penup()
        self.goto(150,-400)
        self.pendown()
        self.goto(150,400)
        self.draw_dash((90,-400))
        self.draw_dash((30,-400))
        self.draw_dash((-30,-400))
        self.draw_dash((-90,-400))
        self.penup()
        self.goto(-150,-400)
        self.pendown()
        self.goto(-150,400)



    def draw_dash(self, position):
        self.setheading(90)
        self.penup()
        self.goto(position)
        for i in range(50):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
