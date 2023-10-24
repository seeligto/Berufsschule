import random
geworfen = []
while (wuerfel_zahl := random.randint(1, 6)) != 6:
    geworfen.append(wuerfel_zahl)
geworfen.append(6)
print(geworfen)
print("Anzahl: ", len(geworfen))
