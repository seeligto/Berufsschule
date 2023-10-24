spieler = ["Armin", "Batu", "Kai", "Sven", "Paul", "Milan"]
ersatz  = ["Chris", "Dennis", "Emin", "Goran", "Luca", "Nico"]
kader = spieler+ersatz
print("(1) Startaufstellung anzeigen")
print("(2) Ersatzspieler anzeigen")
print("(3) Kader anzeigen")

anzeige = int(input("Anzeigewunsch (1-3): "))

def zeige_startaufstellung():
    print("----------------")
    print("Startaufstellung")
    print("----------------")
    for i in range(0, len(spieler)):
        print(spieler[i])

def zeige_ersatzspieler():
    print("----------------")
    print("Ersatzspieler")
    print("----------------")
    for o in range(0, len(ersatz)):
        print(ersatz[o])

def zeige_kader():
    print("----------------")
    print("Kader")
    print("----------------")
    for p in range(0, len(spieler+ersatz)):
        print(kader[p])



if anzeige == 1: zeige_startaufstellung()

elif anzeige == 2: zeige_ersatzspieler()   

elif anzeige == 3: zeige_kader()
