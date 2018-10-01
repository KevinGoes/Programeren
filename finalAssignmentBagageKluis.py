def toonAantalKluizenVrij():
    invoer = open('kluizen.txt', 'r')
    aantalRegels = 12 - len(invoer.readlines())
    invoer.close()
    return aantalRegels


def nieuweKluis():
    if toonAantalKluizenVrij() > 0:
        kluizen = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
        invoer = open('kluizen.txt', 'r')
        for i in range(12 - toonAantalKluizenVrij()):
            tmp = invoer.read(2)
            if ';' in tmp:
                tmp = tmp.replace(';', '')
                kluizen.remove(tmp)
            else:
                kluizen.remove(tmp)
            invoer.readline()
        return kluizen
    else:
        return 'geenkluizenvrij'


def kluisOpenen(kluisNummer, wachtwoord3):
    invoer = open('kluizen.txt', 'r')
    kluizenLijst = []
    for i in range(12 - toonAantalKluizenVrij()):
        tmp = invoer.readline()
        tmp = tmp.replace('\n', '')
        tmp = tmp.split(';')
        if tmp[0] == kluisNummer:
            if tmp[1] == wachtwoord3:
                return 'toegang'
            else:
                return 'foutWachtwoord'
        else:
            pass


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
        if nieuweKluis() == 'geenkluizenvrij':
            print('Er zijn geen kluizen vrij! \n')
        else:
            print('Kluizen', nieuweKluis(), 'zijn nog vrij!')
            invoer2 = input('Welke kluis wilt u? ')
            while invoer2 not in '1234567890':
                print(invoer2, 'is geen kluisnummer!')
                invoer2 = input('probeer het nogmaals! ')
            wachtwoordInvoer = input('Welk wachtwoord wilt u gebruiken? ')
            invoerBestand = open('kluizen.txt', 'a+')
            invoerBestand.readlines()
            invoerBestand.write('\n' + invoer2 + ';' + wachtwoordInvoer)
            print('Kluis ', invoer2, ' is van u! \n')
            invoerBestand.close()
            wiltDoorgaan = input('Wilt u nog wat weten? ')
        wiltDoorgaan = input('Wilt u nog wat weten? ')
        if wiltDoorgaan == 'ja':
            doorgaan = 'True'
        else:
            break
    elif invoer == '3':
        kluisNummer = input('Welk kluisnummer heeft u? ')
        wachtwoord3 = input('Welk wachtwoord heeft u? ')
        if kluisOpenen(kluisNummer, wachtwoord3) == 'toegang':
            print('U heeft toegang tot uw kluis')
        elif kluisOpenen(kluisNummer, wachtwoord3) == 'foutWachtwoord':
            print('Fout wachtwoord!')
        else:
            print('Deze kluis is niet in gebruik!')
        print('\n')
        wiltDoorgaan = input('Wilt u nog wat weten? ')
        if wiltDoorgaan == 'ja':
            doorgaan = 'True'
        else:
            break

    else:
        print('4')