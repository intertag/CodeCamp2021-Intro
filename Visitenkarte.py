print("Bitte Daten eingeben für Visitenkarte")
vorname_1 = input("1. Vorname?")
vorname_2 = input("2. Vorname?")
nachname = input("Nachname?")

print("Hier nun Ihre Visitenkarte:")
print(f"Erster Vorname: {vorname_1}")
if vorname_2 != "":
    print(f"Zweiter Vorname: {vorname_2}")
print(f"Nachname: {nachname}")
