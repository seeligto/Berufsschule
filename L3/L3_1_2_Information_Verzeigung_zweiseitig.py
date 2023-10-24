mindestPreis = 24.99
gebot = float(input("Geben sie ihr Gebot:"))
if gebot<= mindestPreis:
    print("Ihr Angebotspreis liegt unterhalb des Mindestpreises!")
else:
    print("Herzlichen Glückwunsch, Sie haben den Artikel erworben")
