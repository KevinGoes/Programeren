def kwadraten_som(grondgetallen):
    for getal in grondgetallen:
        if getal < 0:
            grondgetallen.remove(getal)
    return grondgetallen[0]**2 + grondgetallen[1]**2 + grondgetallen[2]**2


grondgetallen = [5, -2, -19, 16, 9]
kwadraten_som(grondgetallen)

print(kwadraten_som(grondgetallen))