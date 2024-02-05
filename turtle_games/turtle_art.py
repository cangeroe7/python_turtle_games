import turtle
import random

# Create a new screen
screen = turtle.Screen()

# Set the title of the screen
screen.title("Random Turtle Art")

# Define a list of colors to choose from
colors = ['red', 'blue', 'green', 'yellow', 'purple']

# Set up the turtle object
t = turtle.Turtle()
t.speed(0)
screen.bgcolor("lightblue")
t.color(random.choice(colors))
# Define a function to draw a random shape 
def draw_shape():
    # Choose a random color for the shape 
    t.color(random.choice(colors))

    # Draw a random shape or move
    if random.random() < 0.5:
        t.begin_fill()
        t.circle(random.randint(10, 100))
        t.end_fill()
    else:
        t.penup()
        t.forward(random.randint(10, 100))
        t.right(random.randint(0, 360))
        t.pendown()

# Set up the loop to draw the art
def draw_art(x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(random.randint(2, 5)):
        # Draw random shapes and lines
        for j in range(random.randint(2, 5)):
            draw_shape()

# Call the draw_art function when the screen is clicked
screen.onclick(draw_art)

# Exit the turtle program
turtle.done()
