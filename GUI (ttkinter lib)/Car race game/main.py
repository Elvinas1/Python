from turtle import Screen
from drawroad import Drawroad
from player import Player
from car_manager import Carmanager
from scoreboard import Scoreboard
import time
screen = Screen()


screen.setup(600,800)
screen.tracer(0)

drawroad = Drawroad()
player = Player()
car_manager = Carmanager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move_right, 'Right')
screen.onkey(player.move_left, 'Left')


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    car_manager.refresh()
    car_manager.move()

    if player.xcor()>150 or player.xcor()<-150:
        scoreboard.game_over()
        game_is_on = False

    for car in car_manager.cars:

        if abs(car.xcor()- player.xcor())< 1 and player.distance(car)<70:
            scoreboard.game_over()
            game_is_on = False

        if car.ycor()< -250:
            scoreboard.increase_score()
            car.hideturtle()
            car_manager.cars.remove(car)


    screen.update()




























screen.exitonclick()