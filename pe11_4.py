import csv

def inlezen(Informatie1, Informatie2):
    with open('artikelPrijs.csv', 'r') as myCSVFile:
        lezen = csv.DictReader(myCSVFile, delimiter=';')
        informatie1Lst = []
        informatie2Lst = []
        for regel in lezen:
            tmp = regel[Informatie1]
            tmp = float(tmp)
            informatie1Lst.append(tmp)
            informatie2Lst.append(regel[Informatie2])
        return informatie1Lst, informatie2Lst


prijs, naam = inlezen('Prijs', 'Naam')
hoogstePrijs = max(prijs)
naamHoogstePrijs = naam[prijs.index(hoogstePrijs)]
print('Het duurste artikel is {} en dat kost {} Euro'.format(naamHoogstePrijs, hoogstePrijs))

voorraad, artikel = inlezen('Voorraad', 'Artikelnummer')
minsteVoorraad = min(voorraad)
artikelnummerMinsteVoorraad = artikel[voorraad.index(minsteVoorraad)]
minsteVoorraad = int(minsteVoorraad)
print('Er zijn slecht {} exemplaren in voorraad van het product met nummer {}'.format(minsteVoorraad, artikelnummerMinsteVoorraad))

totaleVoorraad = sum(voorraad)
totaleVoorraad = int(totaleVoorraad)
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaleVoorraad))