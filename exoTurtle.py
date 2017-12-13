import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor('blue')
    
    brad = turtle.Turtle()
    brad.speed(1000)
    brad.shape('turtle')
    
    for i in range(360):
        brad.color('red') if i%2 == 0 else brad.color('yellow')
        for a in range(4):
            brad.fd(100)
            brad.right(1)
        brad.right(1)
    
    window.exitonclick()

draw_square()
