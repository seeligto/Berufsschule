def hoeheBerechnen(iTemp):
    hoehe = 30000-300*iTemp
    return hoehe
#main
print("Programm zur Berechnung der Höhe anhand der Siedetemperatur")
sTmp=float(input("Siedetemperatur in Grad Celsius: "))

print("Die Höhe beträgt:",hoeheBerechnen(sTmp),"Meter")