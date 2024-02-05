import turtle
import random
import time

# makes a screen and sets the background color to lightblue
screen = turtle.Screen()
screen.bgcolor('lightblue')  

# creates player one, makes it blue and shaped like a turtle
player_one = turtle.Turtle()
player_one.color('blue')
player_one.shape('turtle')

# creates player two by cloning player one and changing it's color
player_two = player_one.clone()
player_two.color('red')

# positions player one and player two
player_one.penup()
player_one.goto(-300, 200)
player_two.penup()
player_two.goto(-300, -200)

# draws a finish line
player_one.goto(300, -250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish!', font=24)

# returns player one to it's starting position
player_one.penup()
player_one.color('blue')
player_one.goto(-300, 200)
player_one.right(90)

# puts the pen down for both players so we can see the line 
player_one.pendown()
player_two.pendown()

die = [1, 2, 3, 4, 5, 6]
# runs until one of the two turtles has crossed the finish line
for i in range(30):
    if player_one.pos() >= (300, 250):
        player_one.penup()
        player_one.goto(0,0)
        player_one.write(".       Player One Won!", font=48)
        print("Player One Wins the Race!")
        break
    elif player_two.pos() >= (300, -250):
        player_two.penup()
        player_two.goto(0,0)
        player_two.write(".        Player Two Won!", font=48)
        print("Player Two Wins the Race!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30 * die_roll)
        time.sleep(1)
        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll2)
        time.sleep(1)

# keeps the screen running 
turtle.done()