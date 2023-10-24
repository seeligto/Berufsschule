mathe=float(input("Mathenote: "))
deutsch=float(input("Deutschnote: "))
englisch=float(input("Englischnote: "))
avg=(mathe+deutsch+englisch)/3
if mathe>4.0 or deutsch>4.0 or englisch>4.0:
    print("Mathenote: ",mathe)
    print("Deutschnote: ", deutsch )
    print("Englischnote: ",englisch)
    print("Die Aufnahme ist nicht möglich!")
elif avg>3:
    print("Mathenote: ",mathe)
    print("Deutschnote: ", deutsch )
    print("Englischnote: ",englisch)
    print("Die Aufnahme ist nicht möglich!")
else:
    print("Mathenote: ",mathe)
    print("Deutschnote: ", deutsch)
    print("Englischnote: ",englisch)
    print("Die Aufnahme ist möglich!")