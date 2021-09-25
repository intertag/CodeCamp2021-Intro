
print("Hello World")
#  Kommentar

print(7)  # Integer (Ganze Zahlen)
print(7.5)  # Float (Fließkomma Zahlen)
print('String Test')  # String (Text)
print(True)  # Boolean (Wahr)
print(False)  # Boolean (Falsch)

alter = 18
is_maennlich = False
schuhgroesse = 39
print(alter)
print(f"Alter: {alter} Jahre. Ist Männlich? {is_maennlich} Schuhgröße: {schuhgroesse}")


# alter = input("Wie alt bist du?")
# print(alter)

if schuhgroesse == 40:
    print("Genau 40")
elif schuhgroesse >= 40:
    print("Schuhgröße größer oder gleich 40")
else:
    print("Schuhgröße kleiner 40")

lottozahlen_liste = [2, 4, 6, 8, 10, 12]
# print(f"Lotto-Zahl 1: {lottozahlen_liste[0]}")
# print(f"Lotto-Zahl 2: {lottozahlen_liste[1]}")
# print(f"Lotto-Zahl 3: {lottozahlen_liste[2]}")

for n in range(6):  # zähle n hoch (+1), solange n kleiner als 6 ist
    # print(f"n ist jetzt {n}")
    print(f"Lotto-Zahl {n+1}: {lottozahlen_liste[n]}")

x = 0
while x < 6:
    print(f"Lotto-Zahl {x+1}: {lottozahlen_liste[x]}")
    x = x + 1

