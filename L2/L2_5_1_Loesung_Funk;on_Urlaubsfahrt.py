def benzinkosten(iBenzinpreis,iVerbrauchDesAutos,iLaengeDerStrecke):
    LiterVerbraucht = iVerbrauchDesAutos/100*iLaengeDerStrecke
    kosten=iBenzinpreis*LiterVerbraucht
    return kosten
#main
BenzPreis=float(input("Benzinpreis: "))
Verbrauch=float(input("Verbrauch (in L/100km): "))
Strecke=float(input("Gefahrene Strecke (in km): "))
kosten=benzinkosten(BenzPreis,Verbrauch,Strecke)
print("Die Fahrtkosten betragen: ",kosten,"€")