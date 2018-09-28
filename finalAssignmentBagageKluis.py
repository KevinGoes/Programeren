def toonAantalKluizenVrij():
    invoer = open('kluizen.txt', 'r')
    aantalRegels = 12 - len(invoer.readlines())
    invoer.close()
    return aantalRegels


def nieuweKluis():
    invoer = open('kluizen.txt', 'r')
    kluizenVrij = 12 - len(invoer.readlines())
    invoer.close()
    if kluizenVrij == 8:
        return kluizenVrij


def kluisOpenen():
    asdf


def kluisTeruggeven():
    asdf


doorgaan = 'True'
while doorgaan == 'True':
    doorgaan = 'False'
    print('1. Ik wil weten hoeveel kluizen er nog vrij zijn')
    print('2. Ik wil een nieuwe kluis')
    print('3. Ik wil even iets uit mijn kluis halen')
    print('4. Ik geef mijn kluis terug \n')
    invoer = input('Toets uw optie in: ')

    while invoer != '1' and invoer != '2' and invoer != '3' and invoer != '4':
        invoer = input('Toets uw optie in: ')

    if invoer == '1':
        print('Er zijn in totaal', toonAantalKluizenVrij(), 'kluizen vrij! \n')
        wiltDoorgaan = input('Wilt u nog wat weten? ')
        if wiltDoorgaan == 'ja':
            doorgaan = 'True'
        else:
            break
    elif invoer == '2':
        if nieuweKluis() == 8:
            print('Er zijn geen kluizen vrij! \n')
            wiltDoorgaan = input('Wilt u nog wat weten? ')
            if wiltDoorgaan == 'ja':
                doorgaan = 'True'
            else:
                break
        else:
            print('Kut')
    elif invoer == '3':
        print('3')
    else:
        print('4')