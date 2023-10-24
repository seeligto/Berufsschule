gehalt = int(input("Geben Sie das Gehalt ein: "))
wochencount = 1
taschengeld = 0.01
while taschengeld < gehalt:
    wochencount+=1
    taschengeld*=2
monate=wochencount/4
print("Monate bis Taschengeld höher: ", monate)