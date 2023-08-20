from turtle import Turtle, colormode
import random

colormode(255)

class Carmanager:
    def __init__(self):
        self.cars=[]
        self.location = [(0,400), (-60,400), (-120,400), (60,400),(120,400)]
        self.create_Car()





    def create_Car(self):
        new_car = Turtle()
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        new_car.color(r,g,b)

        new_car.penup()
        new_car.shape('square')
        new_car.setheading(270)
        new_car.shapesize(2.5,4)
        new_car.goto(random.choice(self.location))
        self.cars.append(new_car)

    def refresh(self):

        if self.cars[-1].ycor()<=300:
            self.create_Car()

    def move(self):
        for c in self.cars:
            c.forward(10)

