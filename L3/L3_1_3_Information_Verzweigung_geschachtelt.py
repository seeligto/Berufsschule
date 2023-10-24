mietPreis = float(input("Geben Sie Ihren Mietpreis:"))
if mietPreis<500.00:
    mietPreis=mietPreis*0.02
elif mietPreis<1000.00:
    mietPreis=mietPreis*0.05
elif mietPreis>=1000.00:
    mietPreis*=0.07
print("Ihr Zuschuss beträgt: ", mietPreis)
