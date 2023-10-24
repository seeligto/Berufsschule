alter=int(input("Alter angeben:"))
anzahlTheorieStunden=int(input("Anzahl Theoriestunden angeben:"))
if alter>=17 & anzahlTheorieStunden>=16:
    print("Sie sind zur Prüfung zugelassen")
else:
    print("Pechgehabt, sie sind zu Jung oder haben zu wenig Theoriestunden")