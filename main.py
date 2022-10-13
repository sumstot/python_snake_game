from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Python Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()

scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    scoreboard

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_scoreboard()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
