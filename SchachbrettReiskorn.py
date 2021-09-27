summe = 0

for feld in range(64):
    reiskoerner = 2 ** feld
    summe += reiskoerner
    print(f"Feld {feld + 1} = {reiskoerner:>27,} Reiskörner und damit insgesamt"
          f"{summe:>28,} Reiskörner")

gewicht_in_gramm = summe * 0.02  # Ein Reiskorn wiegt ca. 0,02 Gramm
gewicht_in_tonnen = gewicht_in_gramm / 1000 / 1000
print()
print("Wenn ein Reiskorn 0,02 Gramm wiegt, wiegen die gesamten"
      f" Reiskörner {gewicht_in_tonnen:,.0f} Tonnen")
