import turtle


def zeichne_richtung(himmelsrichtung):
    heading = hole_heading(himmelsrichtung)
    turtle.setheading(heading)
    turtle.forward(10)


def hole_heading(richtung):
    if richtung == "N":
        return 90
    if richtung == "O":
        return 0
    if richtung == "S":
        return 270
    if richtung == "W":
        return 180


richtungen = "N W S N O W S O W N W N"
richtungen_liste = richtungen.split()
for n in richtungen_liste:
    zeichne_richtung(n)

turtle.done()
