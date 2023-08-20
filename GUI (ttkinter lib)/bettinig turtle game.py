import turtle
from turtle import Turtle, Screen, colormode
import random

#t=Turtle()
colormode(255)
#t.shape('triangle')
#t.speed('fastest')
screen = Screen()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb= (r,g,b)
    return rgb
#for i in range(100):
#    t.dot(20,random_color())
 #   t.goto(random.randint(-300,300), random.randint(-300,300))



#def draw(angle):
#    for i in range(int(360/angle)):
#        t.color(random_color())
#       t.circle(50)
#       t.setheading(t.heading()+angle)
#draw(1)

screen.setup(1920,1080)
#result = screen.textinput(title='Calculate', prompt='5*4=?')
turtles = []
y = -400
for i in range(20):
    new_turtle = Turtle(shape='turtle')
    new_turtle.pencolor('red')
    new_turtle.color(random_color())
    new_turtle.speed('fastest')
    turtles.append(new_turtle)
    new_turtle.goto(-200, y)
    y+= 40
print(turtles)
finish = False
while True:

        for turtle in turtles:
            turtle.forward(random.randint(1,20))
            if turtle.xcor()>250:
                turtle.write('I won', font=('Arial', 30, 'bold'))
                finish = True
                break
        if finish:
            break
#def move():
    #t.forward(10)
#def turn_left():
    #t.left(90)


#screen.listen()
#screen.onkey(key= 'space', fun=move)
#screen.onkey(key= 'l', fun=turn_left)


screen.exitonclick()