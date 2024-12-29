from turtle import Screen
import time
from Snake import Snake
from food import Food
from ScoreBoard import Board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
board = Board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    screen.update()                             #updating after moving forward
    screen.update()
    time.sleep(0.1)               
    snake.move()
    
    #Collision Detection
    #with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        board.increase_score()
    
    # with wall
    if snake.head.xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
       board.reset()
       snake.reset()
    
    #with body
    for segments in snake.segments[1:]:
       
        if snake.head.distance(segments) < 10:
            board.reset()
            snake.reset()
    
screen.exitonclick()
