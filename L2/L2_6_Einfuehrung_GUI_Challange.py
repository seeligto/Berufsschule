from tkinter import*

def berechnen():
     zahl_1 = float(tf_zahl1.get())
     ergebnis = zahl_1 * 2
     lb_ergebnis1_ausgabe.config(text=ergebnis)
     zahl_1 = float(tf_zahl1.get())
     ergebnis2 = zahl_1/2
     lb_ergebnis2_ausgabe.config(text=ergebnis2)

#main
fenster = Tk()
fenster.title("Beispiel-GUI: Rechner")
# Elemente werden in einer Tabellenstruktur angeordnet:
# 1. Zeile
lb_zahl1 = Label(fenster, anchor=W, width=17, text="Zahl eingeben:")
lb_zahl1.grid(row = 0, column = 0)
tf_zahl1 = Entry(fenster)
tf_zahl1.grid(row = 0, column = 1)
# 2. Zeile
lb_ergebnis1 = Label(fenster, text="Verdopplung der Zahl:")
lb_ergebnis1.grid(row = 1, column = 0)
lb_ergebnis1_ausgabe = Label(fenster, bg="white", relief = SUNKEN, anchor=W, width = 17)
lb_ergebnis1_ausgabe.grid(row = 1, column = 1)


#3. Zeile
lb_ergebnis2 = Label(fenster,text="Halbierung der Zahl:")
lb_ergebnis2.grid(row = 2, column = 1)
lb_ergebnis2_ausgabe = Label(fenster, bg="white", relief = SUNKEN, anchor=W, width = 17)
lb_ergebnis2_ausgabe.grid(row = 2, column = 1)

# Umrechnungsschaltfläche wird in 4. Zeile rechts hinzugefügt
bt_umrechnen = Button(fenster, text="Berechnung starten", command=berechnen)
bt_umrechnen.grid(row = 3, column = 1)



