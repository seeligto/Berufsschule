karteAbiBall = 30
anzahlBestellungen = int(input("Wie viel Abiballkarten wollen sie bestellen? "))
if(anzahlBestellungen>=3):
    betrag = anzahlBestellungen*karteAbiBall
    betrag*=0.8
else:
    betrag = anzahlBestellungen*karteAbiBall
print("Die Bestellung kostet ", betrag, "€")