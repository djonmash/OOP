import turtle
import math
import random
win = turtle.Screen()
win.setup(1920, 1080)
win.bgcolor('cyan')
width = win.getcanvas().winfo_screenwidth()
height = win.getcanvas().winfo_screenheight()
radius = width/2
rainbow_colours = [(1.0, 0, 0), (1.0, 0.5, 0.0), (1.0, 1.0, 0),
 (0, 1.0, 0), (0, 0, 1), (0.19, 0.17, 0.37), (0.54, 0, 1)]
rainbow = turtle.Turtle("circle")
rainbow.penup()
rainbow.goto(-960, -540)
rainbow.pendown()
rainbow.speed(0)
rainbow.left(90)
for band in range(7):
    rainbow.color(rainbow_colours[band])
    rainbow.begin_fill()
    circumference = 2 * math.pi * radius
    stepLength = circumference / 36
    for step in range(18):
        rainbow.forward(stepLength)
        rainbow.right(10)

    rainbow.forward(stepLength)
    rainbow.right(90)
    rainbow.forward(100)
    rainbow.right(90)
    radius -= 100
    circumference = 2 * math.pi * radius
    stepLength = circumference / 36
    for step in range(18):
        rainbow.forward(stepLength)
        rainbow.left(10)

    rainbow.forward(stepLength)
    rainbow.right(90)
    rainbow.forward(100)
    rainbow.end_fill()
    rainbow.right(180)
    rainbow.forward(100)
    rainbow.left(90)
clouds = []
for i in range(15):
    t = turtle.Turtle("turtle")
    t.speed(0)
    t.penup()
    t.goto(random.randint(-width/2, width/2),
            random.randint(0, height/2))
    t.hideturtle()
    t.pencolor('grey')
    t.fillcolor('white')
    t.pendown()
    t.pensize(5)
    t.begin_fill()
    clouds.append(t)
for i in range(4):
    for cloud in clouds:
        cloud.circle(50, 180)
        cloud.right(90)

for cloud in clouds:
    cloud.end_fill()
    
win.exitonclick()