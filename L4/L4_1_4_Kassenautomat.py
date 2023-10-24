einkaufsPreis = float(input("Geben Sie Ihren Einkaufspreis: "))
if einkaufsPreis>50 and einkaufsPreis<=100:
    print("Endpreis: ", einkaufsPreis*0.95)
elif einkaufsPreis>100:
    print("Endpreis: ", einkaufsPreis*0.9)
else:
    print("Endpreis: ", einkaufsPreis)