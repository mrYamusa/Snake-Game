from turtle import Turtle, Screen
import time
import snake, food
from score import Score

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
score = Score()
screen.listen()

food = food.Food()

snake = snake.Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

gameon = True
while gameon:
    time.sleep(0.1)
    screen.update()
    snake.moveTurtle()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.addscore()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gameon = False
        score.gameover()
    for trtl in snake.turtles:
        if trtl == snake.head:
            pass
        elif snake.head.distance(trtl) < 10:
            gameon = False
            score.gameover()

screen.exitonclick()