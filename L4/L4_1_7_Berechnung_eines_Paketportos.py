def berechne_porto(gewicht, laenge, breite, hoehe):
    if gewicht <= 1 and laenge <= 30 and breite <= 30 and hoehe <= 15:
        return 'XS', 3.95
    elif gewicht <= 2 and laenge <= 60 and breite <= 30 and hoehe <= 15:
        return 'S', 5.95
    elif gewicht < 5 and laenge <= 120 and breite <= 60 and hoehe <= 45:
        return 'M', 9.95
    else:
        return 'Zu groß', None

gewicht = float(input("Geben Sie das Gewicht des Pakets ein: "))
laenge = float(input("Geben Sie die Länge des Pakets ein: "))
breite = float(input("Geben Sie die Breite des Pakets ein: "))
hoehe = float(input("Geben Sie die Höhe des Pakets ein: "))

groesse, porto = berechne_porto(gewicht, laenge, breite, hoehe)

if porto is None:
    print("Das Paket ist für den Transport zu groß und wird abgelehnt.")
else:
    print(f"Es handelt sich um Paketgröße: ",groesse)
    print(f"Das Porto beträgt: ", porto)
