import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")
    
    brad = turtle.Turtle()
    brad.shape("arrow")
    brad.color("blue", "green")
    brad.speed('normal')
    #之前寫成turtle.XXX但發現根本不是這樣寫，要寫成brad.XXX才行

    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

draw_square()