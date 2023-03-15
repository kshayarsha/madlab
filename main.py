from pandas import *
from turtle import *


class Score:
    def __init__(self):
        self.score = 0


t1 = Turtle()
screen = Screen()
screen.screensize(1000,1000)
screen.title('guess all the states')
image = "states.gif"
screen.addshape(image)
t1.shape(image)
guesses=[]
data = read_csv('50_states.csv')
states = data.state.to_list()
sc = Score()
t2 = Turtle()
t2.hideturtle()
t2.penup()
on = True
while on:
    ans = screen.textinput(title=f'{sc.score}/50 correct', prompt='Enter next guess')
    ans = ans.capitalize()
    if ans == 'Exit':
        for stated in states:
            b = data[data.state == stated]
            t2.goto(int(b.x), int(b.y))
            t2.write(stated)
        break
    if ans in states:
        sc.score += 1
        a = data[data.state == ans]
        xc = int(a.x)
        yc = int(a.y)
        t2.goto(xc, yc)
        t2.write(ans)
        if sc.score == 50:
            on = False

screen.exitonclick()
