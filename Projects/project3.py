import turtle

#sets background color to black
turtle.Screen().bgcolor("black")
t = turtle.Turtle()

#moves pen to 10,0
t.penup()
t.goto(10,0)
t.setheading(10)
t.pendown()
t.color("yellow")

#makes circle
for i in range (385):
    t.speed(0)
    t.forward(1)
    t.left(1)


t.penup()
t.goto(10,110)
t.setheading(10)
t.pendown()

for i in range (385):
    t.speed(0)
    t.forward(1)
    t.left(1)
   

t.penup()
t.goto(10,-110)
t.setheading(10)
t.pendown()

for i in range (385):
    t.speed(0)
    t.forward(1)
    t.left(1)

t.penup()
t.goto(-102,-185)
t.setheading(0)
t.pendown()

#makes rectangle
for i in range (4):
    t.forward(200)
    t.left(90)
    t.forward(75)
    t.left(90)
    t.speed(10)

t.penup()
t.goto(-47.5,-185)
t.setheading(10)
t.pendown()

for i in range (385):
    t.speed(0)
    t.forward(1)
    t.left(1)

t.penup()
t.goto(61.5,-185)
t.setheading(10)
t.pendown()

for i in range (385):
    t.speed(0)
    t.forward(1)
    t.left(1)

turtle.exitonclick()