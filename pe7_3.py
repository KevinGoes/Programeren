def aantalRegels():
    invoer = open('kaartnummers.txt', 'r')
    telRegels = invoer.readlines()
    invoer.close()
    return len(telRegels)


def grootsteGetal():
    invoer = open('kaartnummers.txt', 'r')
    getalLijst = []
    n = aantalRegels()
    i = 0
    while i < n:
        getalLijst.append(invoer.read(6))
        invoer.readline()
        i += 1
    invoer.close()
    for i in aantalRegels():
        gevonden = getalLijst.index(i)
        if gevonden == 1:
            gevonden = 1
    return max(getalLijst)


print('Deze file telt', aantalRegels(), 'regels')
print('En het grootste getal is', grootsteGetal(), )

