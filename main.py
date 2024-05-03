import turtle

uzbek = turtle.Turtle()



def braw_square(x, y, length):
    uzbek.penup()
    uzbek.home()
    uzbek.goto((x, y))
    uzbek.color("red")
    uzbek.pendown()

    for storona in range(4):
        uzbek.forward(length)
        uzbek.right(90)


def draw_square(length):
    uzbek.penup()
    uzbek.home()
    uzbek.color("black")
    uzbek.forward(150)
    uzbek.pendown()
    uzbek.forward(length)
    uzbek.penup()

turtle.done()``