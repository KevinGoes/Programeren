def gemiddelde(zin):
    lijstZin = zin.split(' ')
    lengteLijst = len(lijstZin)
    i = 0
    letterAantal = []
    while i < lengteLijst:
        letterAantal.append(len(lijstZin[i]))
        i += 1
    return sum(letterAantal) / lengteLijst


zin = input("Vul een willekeurige zin in: ")
print(gemiddelde(zin))

