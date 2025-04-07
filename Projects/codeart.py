# ###############################################
# ### SETUP ###
import turtle
# ###############################################

t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("purple")
t.pendown()

for i in range(2):
    t.forward(100)

for i in range(2):
    t.down(50)


# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################