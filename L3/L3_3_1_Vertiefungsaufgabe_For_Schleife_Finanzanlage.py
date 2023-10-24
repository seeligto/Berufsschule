kapital=float(input("Kapital der Finanzanlage: "))
zinsSatz = float(input("Zinsatz in 1. angeben(Bsp.: 5%als 1.05)"))
dauer = int(input("Dauer in Jahre angeben: "))

for i in range(0,dauer):
    kapital*=zinsSatz
print("Nach ", dauer, "Jahren beträgt ihr Kapital: ", kapital)