import turtle
import math
import random
from turtle import *

# f = open("highscore.txt", "r+")
# highscore = f.read()
# f.close()
highscore = 0
title("Turtle Archery")
setup(width=600, height=800, startx=None, starty=0)
bgcolor("skyblue")
build = Turtle()
arrow1 = Turtle()
arrow2 = Turtle()
arrow3 = Turtle()
pointer = Turtle()
arrow1.penup()
arrow2.penup()
arrow3.penup()
pointer.shape("circle")
pointer.shapesize(.6)
pointer.color("gray")
pointer.penup()
build.hideturtle()
pointer.hideturtle()

bowx, bowy = 0, -200
bow = (bowx, bowy)
targetx, targety = 0, 200

delay(0)
# build.hideturtle()
build.speed(0)
build.penup()
build.setpos(0, 425)
build.write("Turtle Archery", False, align="center", font=('Arial', 20, 'bold'))
build.setpos(0, 200)
build.dot(403, 'black')
build.dot(400, 'white')
build.dot(320, 'black')
build.dot(240, 'skyblue')
build.dot(163, 'black')
build.dot(160, 'red')
build.dot(83, 'black')
build.dot(80, 'yellow')
build.dot(33, 'black')
build.dot(30, 'yellow')
build.setpos(-265, -280)
build.write("Arrows left", False, align="left", font=("Arial", 12))
build.setpos(-265, -240)
build.write(f"High Score: {highscore}", False, align="left", font=("Arial", 12))
build.setpos(0, -200)
build.pendown()
build.circle(2)
build.penup()
arrow1.setpos(0, -200)
arrow1.setheading(90)
arrow2.setpos(-240, -300)
arrow3.setpos(-210, -300)


def drag1(x,y):
    pointer.showturtle()
    pointer.setpos(-x*2,-(200+y)*3)
    arrow1.setpos(x,y)
    arrow1.seth(arrow1.towards(bow))


def drag2(x,y):
    pointer.showturtle()
    pointer.setpos(-x*2,-(200+y)*3)
    arrow2.setpos(x,y)
    arrow2.seth(arrow2.towards(bow))
    
def drag3(x,y):
    pointer.showturtle()
    pointer.setpos(-x*2,-(200+y)*3)
    arrow3.setpos(x,y)
    arrow3.seth(arrow3.towards(bow))

def shot1(x,y):
    windx = random.randint(-10, 10)
    windy = random.randint(-10,10)
    pointer.hideturtle()
    posx, posy = pointer.position()
    posx, posy = posx + windx, posy + windy
    arrow1.pendown()
    delay(1)
    arrow1.goto(posx, posy)
    arrow1.penup()
    delay(0)
    arrow2.setpos(bowx, bowy)
    arrow2.ondrag(drag2)
    arrow2.setheading(90)

def shot2(x,y):
    windx = random.randint(-50, 50)
    windy = random.randint(-50,50)
    pointer.hideturtle()
    posx, posy = pointer.position()
    posx, posy = posx + windx, posy + windy
    arrow2.pendown()
    delay(1)
    arrow2.goto(posx, posy)
    arrow2.penup()
    delay(0)
    arrow3.setpos(bowx, bowy)
    arrow3.ondrag(drag3)
    arrow3.setheading(90)

def shot3(x,y):
    windx = random.randint(-10, 10)
    windy = random.randint(-10,10)
    pointer.hideturtle()
    posx, posy = pointer.position()
    posx, posy = posx + windx, posy + windy
    arrow3.pendown()
    delay(1)
    arrow3.goto(posx, posy)
    arrow3.penup()
    delay(0)
    get_score()

def get_score():
    score = 0
    arrows = [arrow1, arrow2, arrow3]
    for arrow in arrows:
        arrX, arrY = arrow.position()
        arrY -= 200
        reach = math.sqrt(arrX**2 + arrY**2)
        if reach < 15:
            score += 50
        elif reach < 40:
            score += 30
        elif reach < 80:
            score += 20
        elif reach < 120:
            score += 10
        elif reach < 160:
            score += 5
        elif reach < 400:
            score += 1
    build.setpos(0, -100)
    if score > int(highscore): 
        build.write(f"New High Score: {score}", False, align='center', font=('Arial', 20))
    else:
        build.write(f"Score: {score}", False, align='center', font=('Arial', 20))
    
    # if score > int(highscore):
    #     f = open("highscore.txt", "w")
    #     f.write(str(score))
    #     f.close()

arrow1.ondrag(drag1)
arrow1.onrelease(shot1)
arrow2.onrelease(shot2)
arrow3.onrelease(shot3)

turtle.done()