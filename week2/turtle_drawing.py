import turtle

myTurtle = turtle.Turtle()
myWindow = turtle.Screen()


myTurtle = turtle.Turtle()
myWindow = turtle.Screen()
myWindow.setup(width=600, height=500)
myWindow.bgcolor('blue')
myTurtle.pensize(3)
myTurtle.shape('turtle')
myTurtle.color('white')
myTurtle.penup()
myTurtle.goto(50, 100)
myTurtle.pendown()
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.forward(100) 
myTurtle.right(90)
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.forward(100) 


myWindow.exitonclick()