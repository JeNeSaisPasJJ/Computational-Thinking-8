# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)

# Section 2: Setup
s1 = create_sprite("lebron2" ,0 ,0)
set_background("basketballcourt")
lives = 3
obstacles = []

# Section 3: Controls
def move_up():
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

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
 	# TODO - code for automatic actions

	if timer % 7 == 0:
		y_position = random.randint(-250, 250)
		s2 = create_sprite("basketball" ,350 ,random.randint(-250, 250))
		s2.setheading(180)
		obstacles.append(s2)


	for s2 in obstacles:
		s2.forward(10)
		if get_distance(s1,s2) < 60:
			lives -= 1
			obstacles.remove(s2)





	window.update()

	if lives <= 0:
		break
	

print("Game Over")