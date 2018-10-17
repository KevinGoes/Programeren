# import time
#
def omzettenASCII(omzetWaarde):
    lijst = list(omzetWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) - 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin


def terugomzettenASCII(omgezetteWaarde):
    lijst = list(omgezetteWaarde)
    i = 0
    omgezetteWaarde = []
    for letter in lijst:
        ASCII = ord(lijst[i]) + 3
        CHAR = chr(ASCII)
        omgezetteWaarde.append(CHAR)
        i += 1
    zin = ''.join(omgezetteWaarde)
    return zin

# print(omzettenASCII('stalling'))
# print(omzettenASCII('wachtwoord'))
# print(omzettenASCII(time.strftime(("%d-%b-%Y, %H:%M:%S"))))
# print(terugomzettenASCII('..*.-*/-.5'))
#

import csv

with open('stalling.csv', 'r', newline='') as myCSVFile:
    lezer = csv.DictReader(myCSVFile, delimiter=',')
    stalling = []
    wachtwoorden = []
    datum = []
    for regel in lezer:
        omgezet = terugomzettenASCII(regel['pq^iifkd'])
        stalling.append(omgezet)
        omgezet = terugomzettenASCII(regel['t^`eqtlloa'])
        wachtwoorden.append(omgezet)
        omgezet = terugomzettenASCII(regel['a^qrj'])
        datum.append(omgezet)
    del stalling[1]
    del wachtwoorden[1]
    del datum[1]

with open('stalling.csv', 'w', newline='') as myCSVFile:
    schrijven = csv.writer(myCSVFile)
    schrijven.writerow(stalling[0])





