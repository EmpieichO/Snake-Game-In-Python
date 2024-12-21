from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect if snake head collides with food
    if snake.snake_head.distance(food) < 17:
        food.refresh()
        snake.snake_extend()
        scoreboard.score_update()

    if snake.snake_head.xcor() > 300 or snake.snake_head.xcor() < -300 or snake.snake_head.ycor() > 300 or snake.snake_head.ycor() < -300:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail or body
    for square in snake.snake_trail[1:len(snake.snake_trail)]:
        if snake.snake_head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
