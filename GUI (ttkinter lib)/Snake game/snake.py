from turtle import Turtle

POSITIONS = [(0,0),(-20,0),(-40,0)]
DISTANCE= 20
UP=90
DOWN=270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in POSITIONS:
            self.add_segments(position)

    def add_segments(self, position):
            new_segment = Turtle(shape='square')
            new_segment.penup()
            new_segment.color('red')
            new_segment.goto(position)
            self.segments.append(new_segment)

    def extend(self):
        self.add_segments(self.segments[-1].position())


    def move(self):
        for seg_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_number - 1].xcor()
            new_y = self.segments[seg_number - 1].ycor()
            self.segments[seg_number].goto(new_x, new_y)

        self.head.forward(DISTANCE)

    def up(self):
        if self.head.heading()!=DOWN:
            if self.head.xcor() - self.segments[1].xcor() > 19 or self.head.xcor() - self.segments[1].xcor() < -19:
                self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            if self.head.xcor() - self.segments[1].xcor() > 19 or self.head.xcor() - self.segments[1].xcor() < -19:
                self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            if self.head.ycor() - self.segments[1].ycor() > 19 or self.head.ycor() - self.segments[1].ycor() < -19:
                self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            if self.head.ycor() - self.segments[1].ycor() > 19 or self.head.ycor() - self.segments[1].ycor() < -19:
                self.head.setheading(RIGHT)
