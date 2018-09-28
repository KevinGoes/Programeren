def lijst(woorden):
    lengteLijst = len(woorden)
    woordenLijst = []
    for i in range(lengteLijst):
        if len(woorden[i]) == 4:
            woordenLijst.append(woorden[i])
    return woordenLijst


woorden = eval(input("Geef lijst met minimaal 10 strings: "))
print(lijst(woorden))