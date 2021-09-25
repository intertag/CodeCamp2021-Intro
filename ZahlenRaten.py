# Zahlenraten: Solange eine Zahl raten, bis die richtige Zahl gefunden wurde

print("Zahlenraten!")
zahl = "6"
is_zahl_gefunden = False
while not is_zahl_gefunden:
    geraten = input("Rate die Zahl: ")
    if geraten == zahl:
        is_zahl_gefunden = True
print(f"Du hast die Zahl gefunden: {zahl}")
