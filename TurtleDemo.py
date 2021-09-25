import turtle
import random


def draw_house(x, y):

    #  bewege dich zu punkt
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()

    #  1. Schritt
    turtle.left(90)
    turtle.forward(50)
    #  2. Schritt
    turtle.right(45)
    turtle.forward(40)
    #  3. Schritt
    turtle.right(90)
    turtle.forward(40)
    #  4. Schritt
    turtle.right(135)
    turtle.forward(55)
    #  5. Schritt
    turtle.left(140)
    turtle.forward(70)
    #  6. Schritt
    turtle.setheading(90)
    turtle.forward(50)
    #  7. Schritt
    turtle.left(135)
    turtle.forward(80)
    #  8. Schritt
    turtle.setheading(0)
    turtle.forward(55)


for n in range(10):
    x_zahl = random.randint(-300, 600)
    y_zahl = random.randint(-300, 600)
    draw_house(x_zahl, y_zahl)

turtle.done()
