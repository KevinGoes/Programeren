import xmltodict

def fileOpen(fileName):
    with open(fileName) as myXMLFile:
        inlezen = myXMLFile.read()
        lijst = xmltodict.parse(inlezen)
        return lijst


stations = fileOpen('stations.xml')
lijst = stations['Stations']['Station']

for station in lijst:
    print(station[lijst])

