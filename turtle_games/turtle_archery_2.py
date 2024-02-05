import turtle
import random
import math

# Angry Bir- I mean Turtle Archery
# Fire a bow from the left side of the screen at some angle
# Try to hit a target on the right side of the screen
# Factor in wind and gravity and try to hit the center of the target


from turtle import *


# Create the Window
setup(width=1200, height=600, startx=None, starty=None)
bowx, bowy = -400, 0
bow = (bowx, bowy)
g = .0025
targdist = 450
build = Turtle()
arrow1 = Turtle()
arrow2 = Turtle()
arrow3 = Turtle()
arrow1.penup()
arrow2.penup()
arrow3.penup()

# Main Menu UI
delay(1)
ht()
build.speed(0)
build.penup()
build.setpos(0,250)
build.write("Turtle Archery", False, align="center", font=('Arial', 20, 'bold'))
build.setpos(bowx + 50, -190)
build.write("Shots Left", False, align="center")
build.setpos(targdist,100)
build.pendown()
build.color('black','red')
build.begin_fill()
build.fd(10)
build.rt(90)
build.fd(200)
build.rt(90)
build.fd(10)
build.rt(90)
build.fd(200)
build.rt(90)
build.end_fill()
build.setpos(targdist,65)
build.color('black','yellow')
build.begin_fill()
build.fd(10)
build.rt(90)
build.fd(130)
build.rt(90)
build.fd(10)
build.rt(90)
build.fd(130)
build.rt(90)
build.end_fill()
build.setpos(targdist,25)
build.color('black','green')
build.begin_fill()
build.fd(10)
build.rt(90)
build.fd(50)
build.rt(90)
build.fd(10)
build.rt(90)
build.fd(50)
build.end_fill()
build.hideturtle()
delay(0)

# Score Script
def score():
    dists = [arrow1.distance(targdist,0), arrow2.distance(targdist,0), arrow3.distance(targdist,0)]
    score = 0
    num = 1
    build.penup()
    build.setpos(-50,30)
    build.pendown()
    build.begin_fill()
    build.color('black','gray')
    build.seth(0)
    for i in range(4):
        build.fd(100)
        build.rt(90)
    build.end_fill()
    build.penup()
    build.setpos(0,0)
    build.seth(270)
    for i in dists:
        if i <= 25:
            score = score + 50
            build.color('Green')
            build.write("Shot " + str(num) +": 50", False, align=('center'), font=('Arial', 15, 'normal'))
            build.fd(20)
            num = num + 1
        elif i <= 65:
            score = score + 3
            build.color('Yellow')
            build.write("Shot " + str(num) +": 3", False, align=('center'), font=('Arial', 15, 'normal'))
            build.fd(20)
            num = num + 1
        elif i <= 100:
            score = score + 1
            build.color('Red')
            build.write("Shot " + str(num) +": 1", False, align=('center'), font=('Arial', 15, 'normal'))
            build.fd(20)
            num = num + 1
        else:
            build.color('Black')
            build.write("Shot " + str(num) + ": 0", False, align=('center'), font=('Arial', 15, 'normal'))
            build.fd(20)
            num = num + 1
    build.color('Black')
    build.write("Score:  " + str(score), False, align=('center'), font=('Arial', 15, 'normal'))

# Gameplay Functions
def dir1(x,y):
    arrow1.setpos(x,y)
    arrow1.seth(arrow1.towards(bow))
    if arrow1.distance(bow) > 100:
        arrow1.fd(arrow1.distance(bow) - 100)

def dir2(x,y):
    arrow2.setpos(x,y)
    arrow2.seth(arrow2.towards(bow))
    if arrow2.distance(bow) > 100:
        arrow2.fd(arrow2.distance(bow) - 100)

def dir3(x,y):
    arrow3.setpos(x,y)
    arrow3.seth(arrow3.towards(bow))
    if arrow3.distance(bow) > 100:
        arrow3.fd(arrow3.distance(bow) - 100)

def shot1(x,y):
    strn = arrow1.distance(bow)/50
    angle = arrow1.heading()
    wind = random.randint(1,21)
    arrow1.setpos(bow)
    arrow1.speed(6)
    i = 0
    while True:
        if arrow1.xcor() > targdist or arrow1.xcor() < -550 or arrow1.ycor() < -200:
            break
        if  i % 10 == 0:
            arrow1.pendown()
        elif i % 5 == 0:
            arrow1.penup()
        (tempx, tempy) = arrow1.position()
        arrow1.setpos(tempx + strn*math.cos(math.pi/180*angle), tempy + strn*math.sin(math.pi/180*angle)-(i*(1+wind/20)*g))
        arrow1.seth(towards(tempx,tempy))
        i = i + 1
    arrow1.penup()
    arrow2.setpos(bow)

def shot2(x,y):
    strn = arrow2.distance(bow)/50
    angle = arrow2.heading()
    wind = random.randint(1,21)
    arrow2.setpos(bow)
    arrow2.speed(6)
    i = 0
    while True:
        if arrow2.xcor() > targdist or arrow2.xcor() < -550 or arrow2.ycor() < -200:
            break
        if  i % 10 == 0:
            arrow2.pendown()
        elif i % 5 == 0:
            arrow2.penup()
        (tempx, tempy) = arrow2.position()
        arrow2.setpos(tempx + strn*math.cos(math.pi/180*angle), tempy + strn*math.sin(math.pi/180*angle)-(i*(1+wind/20)*g))
        arrow2.seth(towards(tempx,tempy))
        i = i + 1
    arrow2.penup()
    arrow3.setpos(bow)


def shot3(x,y):
    strn = arrow3.distance(bow)/50
    angle = arrow3.heading()
    wind = random.randint(1,21)
    arrow3.setpos(bow)
    arrow3.speed(6)
    i = 0
    while True:
        if arrow3.xcor() > targdist or arrow3.xcor() < -550 or arrow3.ycor() < -200:
            break
        if  i % 10 == 0:
            arrow3.pendown()
        elif i % 5 == 0:
            arrow3.penup()
        (tempx, tempy) = arrow3.position()
        arrow3.setpos(tempx + strn*math.cos(math.pi/180*angle), tempy + strn*math.sin(math.pi/180*angle)-(i*(1+wind/20)*g))
        arrow3.seth(towards(tempx,tempy))
        i = i + 1
    arrow3.penup()
    score()
        
arrow1.setpos(bowx, bowy-2)
arrow1.pendown()
arrow1.circle(2)
arrow1.penup()
arrow1.setpos(bow)
arrow2.setpos(bowx + 40,bowy - 200)
arrow3.setpos(bowx + 60,bowy - 200)

arrow1.ondrag(dir1)
arrow1.onrelease(shot1)
arrow2.ondrag(dir2)
arrow2.onrelease(shot2)
arrow3.ondrag(dir3)
arrow3.onrelease(shot3)
mainloop()