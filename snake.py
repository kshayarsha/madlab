from turtle import Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        y=0
        for x in range(0,3):
          t=Turtle("square")
          t.color('black')
          t.penup()
          t.goto(y,0)
          y-=20
          self.segments.append(t)
    def gen(self):
        t=Turtle("square")
        t.color('black')
        t.speed(0)
        t.penup()
        xc=self.segments[len(self.segments)-1].xcor()
        yc=self.segments[len(self.segments)-1].ycor()
        t.goto(xc,yc)
        self.segments.append(t)
    def moved(self):
        for t in range(len(self.segments)-1,0,-1):
          xc=self.segments[t-1].xcor()
          yc=self.segments[t-1].ycor()
          self.segments[t].goto(xc,yc)
        self.head.forward(20)

    def up(self):
        self.head.setheading(90)
    def down(self):
        self.head.setheading(270)
    def left(self):
        self.head.setheading(180)
    def right(self):
        self.head.setheading(0)

from turtle import *
import random
class Food(Turtle):

  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('blue')
    self.penup()
    self.speed(0)
    self.goto(random.randint(-275,275),random.randint(-275,275))

  def refresh(self):
     self.goto(random.randint(-275,275),random.randint(-275,275))

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.write(f'score:{self.score}', align="center", font=("Arial", 24, "normal"))
        self.hideturtle()
    def inc(self):
        self.score+=1
        self.clear()
        self.write(f'score:{self.score}', align="center", font=("Arial", 24, "normal"))
    def over(self):
        self.goto(0,0)
        self.write('game over', align="center", font=("Arial", 24, "normal"))

from turtle import Screen
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor('white')
screen.title('Snake Game')
screen.tracer(0)
snake=Snake()
food=Food()
sc=Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

on=True
while on:
  screen.update()
  time.sleep(0.1)
  snake.moved()

  for segment in snake.segments[1:]:
      if snake.head.distance(segment)<10:
          on=False
          sc.over()

  if snake.head.distance(food)<15:
      food.refresh()
      sc.inc()
      snake.gen()
  if(snake.head.xcor()>300 or snake.head.ycor()>300 or snake.head.xcor()<-300 or snake.head.ycor()<-300):
      sc.over()
      on=False
      
screen.exitonclick()
