def inlezenBeginstation(stations):
    while True:
        invoer = input('Bij welk station wilt u instappen? ')
        if invoer in stations:
            break
        else:
            print('Deze trein komt niet in ', invoer)
            pass
    return invoer



def inlezenEindstation(stations, beginstation):
    while True:
        invoer = input('Bij welk station wilt u uitstappen? ')
        if invoer in stations and stations.index(beginstation) < stations.index(invoer):
            break
        if invoer in stations:
            print('Eindstation moet verder zijn dan Beginstation \n')
            pass
        else:
            print('Deze trein komt niet in ', invoer)
            pass
    return invoer


def omroepenReis(stations, beginstation, eindstation):
    print('Het beginstation ', beginstation, ' is het ', stations.index(beginstation) + 1, 'e station in dit traject')
    print('Het eindstation ', eindstation, ' is het ', stations.index(eindstation) + 1, 'e station in dit traject')
    print('De afstand bedraagt ', stations.index(eindstation) - stations.index(beginstation), ' station(s)')
    print('De prijs van het kaartje is ', (stations.index(eindstation) - stations.index(beginstation)) * 5, 'euro')



stations = ['Schagen', 'Heerhugowaard', 'Castricum', 'Zaandam', 'Amsterdam Sloterwijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '\'s Hertogenbosch', 'Eindhoven', 'Weerd', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezenBeginstation(stations)
eindstation = inlezenEindstation(stations, beginstation)

print(omroepenReis(stations, beginstation, eindstation))
