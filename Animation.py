import turtle
import time

# Konfiguration Turtle
turtle.hideturtle()
turtle.speed(100)

# Zeichne Kreis
for n in range(100):
    x = 0 + n * 10
    turtle.setpos(x, 0)
    turtle.clear()
    turtle.color('green')
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    time.sleep(0.2)

# Fertig
turtle.done()
