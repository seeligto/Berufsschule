geldBetrag=float(input("Geldbetrag anlegen: "))
zinsSatz=float(input("Zinsatz in %: "))
zins = 1+zinsSatz/100
zielWert=int(input("Welcher Zielwert soll erreicht werde?"))
jahr = 1

while geldBetrag<zielWert:
    geldBetrag*=zins
    jahr+=1
    print("Jahr ",jahr, " : ",geldBetrag)
