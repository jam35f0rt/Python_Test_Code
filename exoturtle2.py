import turtle

def draw_it(turtl):
    for i in range(2):
        turtl.fd(75)
        turtl.rt(45)
        turtl.fd(75)
        turtl.rt(135) 

def draw_flower():
    window = turtle.Screen()
    window.bgcolor('black')
    
    james = turtle.Turtle()
    james.rt(77.5)
    james.speed(50)
    james.shapesize(1,1)
    james.color('cyan','yellow')
    james.shape('turtle')
    james.begin_fill()

    for i in range(36):
        if i%2!=0 :
            james.begin_fill()
        draw_it(james)
        james.rt(10)
        if i%2!=0 :
            james.end_fill()
    james.rt(12.5)
    james.fd(300)
    window.exitonclick()

draw_flower()