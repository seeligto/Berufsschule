wurf = []
wurf.append(int(input("Wurf 1: ")))
wurf.append(int(input("Wurf 2: ")))
wurf.append(int(input("Wurf 3: ")))
wurf.append(int(input("Wurf 4: ")))
wurf.append(int(input("Wurf 5: ")))
wurf.append(int(input("Wurf 6: ")))
wurf.sort(reverse=True)
average=0
print("Bester Wurf: ", wurf[0])
for i in range(len(wurf)):
    average += wurf[i]
print("Schlechtester Wurf: ", wurf[i])
print("Durschnittliche Punktzahl: ", int(average/len(wurf)))