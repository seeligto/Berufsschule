pruefZiffer = k =0
iSBN_Nummer = int(input("ISBN-Nummber: "))
for i in str(iSBN_Nummer):
    k+=1
    pruefZiffer += k*int(i)
pruefZiffer %= 11
print("vollständige ISBN - Nummber: ", str(iSBN_Nummer) + str(pruefZiffer))