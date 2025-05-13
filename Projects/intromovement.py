# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def create_sprite(image_filename, x=0, y=0):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite = turtle.Turtle()
	sprite.shape(image_file)
	sprite.penup()
	sprite.goto(x,y)
	return sprite

window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
set_background("castle")
s1 = create_sprite("character1",0,-200)

# Section 3: define movement controls
 move_up():
	s1.setheading(90)
	s1.forward(10)
   	 
def move_down():
	s1.setheading(270)
	s1.forward(10)
    
def move_left():
	s1.setheading(180)
	s1.forward(10)
    
def move_right():    
	s1.setheading(0)
	s1.forward(10)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

# Section 4: define other controls
# hide and show controls
def hide():
	s1.hideturtle()
def show():
	s1.showturtle()

window.onkeypress(hide, "h")
window.onkeyrelease(show, "h")

def draw ():
	s1.pendown()
def stop_drawing():
	s1.penup()
def erase():
	s1.clear()
def red_pen ():
	s1.color("red")
def green_pen():
	s1.color("green")
def reset(x,y):def
	s1.goto(x,y)

window.onkeypress(red_pen, "r")
window.onkeypress(green_pen, "g")
window.onkeypress(erase, "x")
window.onkeyrelease(stop_drawing, "c")
window.onkeypress(draw, "c")
window.onscreenclick(reset)


s2 = create_sprite("character2",0,-100)

# Section 3: define movement controls
def move_up():
	s2.setheading(90)
	s2.forward(10)
   	 
def move_down():
	s2.setheading(270)
	s2.forward(10)
    
def move_left():
	s2.setheading(180)
	s2.forward(10)
    
def move_right():    
	s2.setheading(0)
	s2.forward(10)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")

# Section 4: define other controls
# hide and show controls
def hide():
	s2.hideturtle()
def show():
	s2.showturtle()

window.onkeypress(hide, "t")
window.onkeyrelease(show, "t")

def draw ():
	s2.pendown()
def stop_drawing():
	s2.penup()
def erase():
	s2.clear()
def red_pen ():
	s2.color("red")
def green_pen():
	s2.color("green")
def reset(x,y):
	s2.goto(x,y)

window.onkeypress(red_pen, "u")
window.onkeypress(green_pen, "j")
window.onkeypress(erase, "b")
window.onkeyrelease(stop_drawing, "q")
window.onkeypress(draw, "q")
window.onscreenclick(reset)

# Section 5: game loop
window.listen()
while True:
	time.sleep(0.01)
	window.update()