import datetime
import csv

vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y at %I:%M:%S")

bestand = 'inloggers.csv'

while True:
    naam = input("Wat is je achternaam? ")
    if naam == 'einde':
        break
    voorl = input("Wat zijn je voorletters? ")
    gbdatum = input("Wat is je geboortedatum? ")
    email = input("Wat is je e-mail adres? ")

    with open(bestand, 'a') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter=';')
        writer.writerow((s, naam, voorl, gbdatum, email))
