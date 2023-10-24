costO = 5.40
costY = 3.20
ges = 0
alter = 1
while alter != 0:
    alter = int(input("Was ist Ihr Alter? "))
    if alter < 16:
        ges += costY
        print(alter, "Jahre: ", costY, "(Gesamt: ", ges, ")")
    else:
        ges += costO
        print(alter, "Jahre: ", costO,"(Gesamt: ", ges, ")")
print("Der Eintritt für alle kostet", ges, "Euro")

