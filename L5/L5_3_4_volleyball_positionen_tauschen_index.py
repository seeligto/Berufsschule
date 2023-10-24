spieler = ["Armin", "Batu", "Kai", "Sven", "Paul", "Milan"]

def startaufstellung_ausgeben():
    print("------------------------")
    print("Neue Startaufstellung")
    print("------------------------")
    for i in range(len(spieler)):
        print(spieler[i])

def mannschaft_umstellen_pos(t_pos,pos):
    spieler[t_pos],spieler[pos] = spieler[pos], spieler[t_pos]
    
    

#Funktionsaufruf
print("Startaufstellung umstellen:")
t_pos = int(input("Tausche Position: "))
pos = int(input("mit Position: "))
mannschaft_umstellen_pos(t_pos-1,pos-1)
startaufstellung_ausgeben()


