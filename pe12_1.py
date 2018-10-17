import xmltodict

def fileOpen(fileName):
    with open(fileName) as myXMLFile:
        inlezen = myXMLFile.read()
        lijst = xmltodict.parse(inlezen)
        return lijst


artikelen = fileOpen('artikelPrijs.xml')
artikelNaam = artikelen['artikelen']['artikel']

for artikel in artikelNaam:
    print(artikel['naam'])