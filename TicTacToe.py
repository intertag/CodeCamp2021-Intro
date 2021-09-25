#  Tic Tac Toe


spielfeld = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def update_spielfeld():
    print("Hier aktualisiere das Spielfeld.")

def zeige_spielfeld():
    print(f" {spielfeld[0]} {spielfeld[1]} {spielfeld[2]}")
    print(f" {spielfeld[3]} {spielfeld[4]} {spielfeld[5]}")
    print(f" {spielfeld[6]} {spielfeld[7]} {spielfeld[8]}")

zeige_spielfeld()

eingabe = input("Spieler X am Zug:")
