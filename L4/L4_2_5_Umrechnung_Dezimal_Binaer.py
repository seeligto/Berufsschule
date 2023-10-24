dezimalZahl = int(input("Geben Sie eine 8-Bit Zahl: "))
binaryStellen = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
binärzahl = ""
if dezimalZahl >= 2**16:
    print("Zahl ist zu groß!")
else:
    for i in range(0, len(binaryStellen)):
        if dezimalZahl>binaryStellen[i]:
            binärzahl += "1"
            dezimalZahl-=binaryStellen[i]
        else:
            binärzahl+= "0"
        
print(binärzahl)