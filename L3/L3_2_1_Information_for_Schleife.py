anfangsBetrag=int(input("Anfangesbetrag: "))
jaehrlicheErhoehung = float(input("Jährliche Erhöhung: "))
alter=int(input("Alter: "))    
taschenGeld = anfangsBetrag
for i in range(6,alter):
    taschenGeld+=taschenGeld*jaehrlicheErhoehung
    print("Alter:", i,": ", taschenGeld)
