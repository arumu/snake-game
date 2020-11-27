from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.square_list[0].distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()

    if snake.square_list[0].xcor() > 290 or snake.square_list[0].xcor() < -295 \
            or snake.square_list[0].ycor() > 290 or snake.square_list[0].ycor() < -290:
        score.game_over()
        game_is_on = False

    for square in snake.square_list[1:]:
        if snake.square_list[0].distance(square) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()