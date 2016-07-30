import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	paul = turtle.Turtle()
	paul = turtle.shape("circle")
	paul = turtle.speed(0.25)
	paul = turtle.color("blue")
	paul.forward(100)
	paul.right(90)
	paul.forward(100)
	paul.right(90)
	paul.forward(100)
	paul.right(90)
	paul.forward(100)

	wendy = turtle.Turtle()
	wendy = turtle.shape("circle")
	wendy = turtle.speed(0.25)
	wendy = turtle.color("blue")
	
	window.exitonclick()	

draw_square()