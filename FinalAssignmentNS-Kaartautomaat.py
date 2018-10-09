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
    print('Het beginstation {} is het {}e station in dit traject'.format(beginstation, stations.index(beginstation) + 1))
    print('Het eindstation {} is het {}e station in dit traject \n'.format(eindstation, stations.index(eindstation) + 1))
    print('De afstand bedraagt {} station(s)'.format(stations.index(eindstation) - stations.index(beginstation)))
    print('De prijs van het kaartje is {} euro'.format((stations.index(eindstation) - stations.index(beginstation)) * 5))


stations = ['Schagen', 'Heerhugowaard', 'Castricum', 'Zaandam', 'Amsterdam Sloterwijk', 'Amsterdam Centraal',
            'Amsterdam Amstel', 'Utrecht Centraal', '\'s Hertogenbosch', 'Eindhoven', 'Weerd', 'Roermond', 'Sittard',
            'Maastricht']
beginstation = inlezenBeginstation(stations)
eindstation = inlezenEindstation(stations, beginstation)

print(omroepenReis(stations, beginstation, eindstation))
