kader = ["Armin", "Batu", "Kai", "Sven", "Paul", "Milan", "Goran", "Chris","Nico", "Dennis", "Emin", "Luca"]

def kader_ausgeben():
    print("------------------------")
    print("Kader")
    print("------------------------")
    for i in range(len(kader)):
        print(kader[i])

def einfuegen_spieler(iName,iInd):
    kader.insert(iInd, iName)

#Funktionsaufruf
name = input("Spielername: ")
ind = int(input("Index: "))
einfuegen_spieler(name,ind)
kader_ausgeben()