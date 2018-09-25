def aantalRegels(fileName):
    invoer = open(fileName, 'r')
    telRegels = invoer.readlines()
    invoer.close()
    return len(telRegels)


def grootsteGetal(fileName):
    invoer = open(fileName, 'r')
    a = invoer.read(6)
    b = invoer.readline()
    c = invoer.read(6)
    d = invoer.readline()
    e = invoer.read(6)
    f = invoer.readline()
    g = invoer.read(6)
    h = invoer.readline()
    i = invoer.read(6)
    j = invoer.readline()
    k = invoer.read(6)
    l = invoer.readline()
    invoer.close()

    getalLijst = [a, c, e, g, i, k]
    return max(getalLijst)


fileName = input("Hoe heet je bestand? ")

print(aantalRegels(fileName))
print(grootsteGetal(fileName))