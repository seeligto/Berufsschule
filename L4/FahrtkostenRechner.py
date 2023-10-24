from tkinter import *

# In dieser Funktion wird die Umrechnung durchgeführt => hier programmieren
def umrechnen():
    Verbrauch_des_Autos = float(tf_Verbrauch_des_Autos.get())
    Laenge_der_Strecke = float(tf_Laenge_der_Strecke.get())
    Benzinpreis = float(tf_Benzinpreis.get())
    Liter_Verbraucht = Verbrauch_des_Autos / 100 * Laenge_der_Strecke
    kosten = Benzinpreis * Liter_Verbraucht
    lb_kosten_ausgabe.config(text=kosten)
    
# Hier beginnt das Hauptprogramm mit der Benutzeroberfläche
fenster = Tk()
fenster.title("BenzinkostenRechner")
# Zeile 1
lb_Verbrauch_des_Autos = Label(fenster, text="Verbrauch des Autos:")
lb_Verbrauch_des_Autos.grid(row = 0, column = 0)
tf_Verbrauch_des_Autos = Entry(fenster)
tf_Verbrauch_des_Autos.grid(row = 0, column = 1)

lb_Laenge_der_Strecke = Label(fenster, text="Länge der Strecke:")
lb_Laenge_der_Strecke.grid(row = 1, column = 0)
tf_Laenge_der_Strecke = Entry(fenster)
tf_Laenge_der_Strecke.grid(row = 1, column = 1)

lb_Benzinpreis = Label(fenster, text="Benzinpreis:")
lb_Benzinpreis.grid(row = 2, column = 0)
tf_Benzinpreis = Entry(fenster)
tf_Benzinpreis.grid(row = 2, column = 1)

#Zeile 2
lb_kosten = Label(fenster, text="Temperatur in Celsius:")
lb_kosten.grid(row = 3, column = 0)
lb_kosten_ausgabe = Label(fenster, fg="blue", bg="white", relief = SUNKEN, width = 17)
lb_kosten_ausgabe.grid(row = 3, column = 1)

#Zeile 3
bt_umrechnen = Button(fenster, text="Ausrechnen, wie viel die Fahrt gekostet hat", command=umrechnen)
bt_umrechnen.grid(row = 4, column = 1)