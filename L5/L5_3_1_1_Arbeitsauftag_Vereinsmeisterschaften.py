platzierungen = ["Matthias Schmitt", "Felix Holzmann", "Sabrina Eggers", "Sebastian Wolf", "Niklas Eisenbaum", "Florian Kuster", "Jan Ackerman", "Erika Ebersbacher"]
gefragt = int(input("Nach welcher Teilnehmer wollen sie schauen? "))
print("Anzahl Teilnehmer: ", len(platzierungen), "Platz ", gefragt, ": ", platzierungen[gefragt-1])