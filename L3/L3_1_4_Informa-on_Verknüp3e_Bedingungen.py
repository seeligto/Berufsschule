mietDauer=int(input("Für wie viele Tage mieten Sie den Oldtimer: "))
wohnOrt = int(input("Wenn Sie aus Stuttgart kommen, geben 1, wenn nicht dann 0: "))
if wohnOrt==0:
    mietDauer*=50
    mietDauer*=0.9
    print("Zu Zahlen: ",mietDauer)
else:
    print("zu zahlen ", mietDauer*50)