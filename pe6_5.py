def kwadraten_som(grondgetallen):
    output_lijst = []
    for getal in grondgetallen:
        if getal > 0:
            getal = getal**2
            output_lijst.append(getal)
    return sum(output_lijst)

print(kwadraten_som([4, 5, 3, -81]))