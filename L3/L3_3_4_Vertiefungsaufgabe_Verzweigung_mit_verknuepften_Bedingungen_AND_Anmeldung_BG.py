mathe=float(input("Mathenote: "))
deutsch=float(input("Deutschnote: "))
englisch=float(input("Englischnote: "))
avg=(mathe+deutsch+englisch)/3
if avg>3:
    print("Mathenote: ",mathe)
    print("Deutschnote: ", deutsch )
    print("Englischnote: ",englisch)
    print("Die Aufnahme ist nicht möglich!")
else:
    print("Mathenote: ",mathe)
    print("Deutschnote: ", deutsch)
    print("Englischnote: ",englisch)
    print("Die Aufnahme ist möglich!")