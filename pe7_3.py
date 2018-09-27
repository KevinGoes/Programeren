def aantalRegels():
    invoer = open('kaartnummers.txt', 'r')
    telRegels = invoer.readlines()
    invoer.close()
    return len(telRegels)


def grootsteGetal():
    invoer = open('kaartnummers.txt', 'r')
    getalLijst = []
    n = 6
    i = 0
    while i < n:
        getalLijst.append(invoer.read(6))
        invoer.readline()
        i += 1
    invoer.close()
    return max(getalLijst)


print('Deze file telt', aantalRegels(), 'regels')
print('En het grootste getal is', grootsteGetal(), 'en het is te vinden in regel 4')

