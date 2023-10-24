fischBestand=3
wdh=0
erwuenschterFischBestand=int(input("Erwünschter Fischbestand: "))

while fischBestand<erwuenschterFischBestand:
    fischBestand*=2
    wdh+=1
    print("Zyglus ", wdh, "Fischbestand = ",fischBestand)