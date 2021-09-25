import turtle


def up():
    turtle.setheading(90)
    turtle.forward(20)


def down():
    turtle.setheading(270)
    turtle.forward(20)


def left():
    turtle.setheading(180)
    turtle.forward(20)


def right():
    turtle.setheading(0)
    turtle.forward(20)


turtle.listen()
turtle.onkey(up, "Up")
turtle.onkey(down, "Down")
turtle.onkey(left, "Left")
turtle.onkey(right, "Right")

turtle.mainloop()

turtle.done()
