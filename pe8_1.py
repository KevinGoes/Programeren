def seizoen(maand):
    if maand > 11 or maand < 3:
        return"Winter"
    elif maand < 6:
        return "Lente"
    elif maand < 9:
        return "Zomer"
    else:
        return "Herfst"


maand = int(input("Welke maand is het? "))
print(seizoen(maand))