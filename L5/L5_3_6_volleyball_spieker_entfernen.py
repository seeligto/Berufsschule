kader = ["Armin", "Batu", "Kai", "Sven", "Paul", "Milan", "Goran", "Chris","Nico", "Dennis", "Emin", "Luca"]

def kader_ausgeben():
    print("------------------------")
    print("Kader")
    print("------------------------")
    for i in range(len(kader)):
        print(kader[i])

def spieler_entfernen(iInd):
    kader.pop(iInd)

#Funktionsaufruf
spieler_entfernen(int(input("Entferne Spieler an der Stelle mit dem Index: ")))
kader_ausgeben()
