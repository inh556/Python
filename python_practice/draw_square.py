import turtle
def draw_square():
	window = turtle.Screen()
	window.bgcolor('white')	
	brad = turtle.Turtle()
	brad.shape('turtle')
	brad.color('red')
	brad.speed(20)	
	for i in range(12):
		for i in range(4):
			brad.forward(100)
			brad.right(90)
		brad.right(30)			
	draw_circle()
	window.exitonclick()
	
def draw_circle():	
	angi = turtle.Turtle()
	angi.shape('classic')
	angi.color('green')
	
	angi.circle(100)
	
	draw_triangle()

def draw_triangle():
	ke = turtle.Turtle()
	ke.shape('arrow')
	ke.color('yellow') 
	for i in range(3):
		ke.forward(100)
		ke.right(120)	

draw_square()
	