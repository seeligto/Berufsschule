days = ["mon","tue","wed","thu","fri","sat","sun"]
for i in range(len(days)):
    temp = float(input(days[0] + ": "))
temp.sort(True)
print("------AUSWERTUNG-----")
print("Höchste Temp: ", temp[0])
print("Niedrigste Temp: ", temp[len(temp)])
print("Temperaturdurschnitt: ", sum(temp)/len(temp))