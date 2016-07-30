import turtle

def draw_shapes(some_shape,sides,size,angle):
	for i in range(1,sides + 1):
		some_shape.forward(size)
		some_shape.right(angle)

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	paul = turtle.Turtle()
	paul.shape("turtle")
	paul.color("blue")
	paul.speed(7)
	for i in range(1,36):
		draw_shapes(paul,4,100,90)
		paul.right(10)
	paul.right(5)
	paul.color("green")
	for i in range(1,72):
		draw_shapes(paul,4,100,90)
		paul.right(5)

	# paul.forward(100)
	# paul.right(90)
	# paul.forward(100)
	# paul.right(90)
	# paul.forward(100)
	# paul.right(90)
	# paul.forward(100)
	# paul.right(90)
	
	wendy = turtle.Turtle()
	wendy.shape("circle")
	wendy.speed(20)
	wendy.color("yellow")
	for i in range(1,130):
		draw_shapes(wendy,3,200,120)
		wendy.right(33)
	wendy.right(5)
	wendy.color("green")
	for i in range(1,30):
		draw_shapes(wendy,3,50,120)
		wendy.right(33)
	wendy.color("blue")
	for i in range(1,30):
		draw_shapes(wendy,3,100,120)
		wendy.right(33)
	wendy.color("black")
	for i in range(1,30):
		draw_shapes(wendy,3,150,120)
		wendy.right(33)

	window.exitonclick()	
# 
draw_square()


def draw_shape(type,sides,color, size, angle):
	window = turtle.Screen()
	window.bgcolor("blue")

	paul = turtle.Turtle()
	paul.shape(type)
	paul.color(color)
	counts = 0
	while (sides < counts):
	# for i in range(1,sides):
		paul.forward(size)
		paul.right(angle)
		counts = counts + 1
		window.exitonclick()

# draw_shape("square",4,"green",150,90)
