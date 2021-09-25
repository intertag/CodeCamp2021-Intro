some_integer = 25
some_string = "Hallo Welt"
some_float = 25.5
some_bool = True

print("Hallo Welt")
print(f"Hallo {some_string}")

if some_bool:
    print("some_bool is True")
else:
    print("some_bool is False")

# while True:
#    print("Dies ist eine Endlosschleife!")

alter = input("Wie alt bist Du?")

zaehler = 0
while zaehler < 10:
    print("Zähler ist kleiner als 10")
    zaehler = zaehler + 1

for n in range(10):
    print(f"n ist {n}")


def hole_ergebnis():
    return 42


ergebnis = hole_ergebnis()
print(f"Ergbnis ist {ergebnis}")

