afstandKM = int(input("Hoeveel Kilometer moet u reizen? "))
leeftijd = int(input("Hoe oud bent u? "))
weekendrit = input("Reist u in het weekend 'ja' of 'nee'? ")

while weekendrit != 'ja' and weekendrit != 'nee':
    print('"' + weekendrit + '"' + ' is geen correcte waarde! Probeer opnieuw!')
    print('\n')
    weekendrit = input("Reist u in het weekend 'ja' of 'nee'? ")


def standaardprijs(afstandKM):
    if afstandKM > 50:
        return afstandKM * 0.60 + 15
    if afstandKM < 0:
        return afstandKM * 0
    else:
        return afstandKM * 0.80


def ritprijs(leeftijd, weekendrit, afstandKM):
    rekenprijs = standaardprijs(afstandKM)
    if weekendrit == 'ja':
        if leeftijd < 12 or leeftijd >= 65:
            return round(rekenprijs * 0.65, 2)
        else:
            return round(rekenprijs * 0.60, 2)
    if weekendrit == 'nee':
        if leeftijd < 12 or leeftijd >= 65:
            return round(rekenprijs * 0.70, 2)
        else:
            return round(rekenprijs, 2)
    else:
        print(weekendrit + " is geen ja of nee!")


print(ritprijs(leeftijd, weekendrit, afstandKM))

