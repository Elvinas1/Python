from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from drowline import Drawer
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(700, 700)
screen.title('Snake game')
screen.tracer()

snake=Snake()
food = Food()
scoreboard = Scoreboard()
drawer = Drawer()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    if snake.head.distance(food)<10:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
    if snake.head.xcor()>281 or snake.head.xcor()<-261 or snake.head.ycor()>261 or snake.head.ycor()<-281:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 15:
            scoreboard.game_over()
            game_is_on = False





screen.mainloop()