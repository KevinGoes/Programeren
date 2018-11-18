import time
from random import randint
import smtplib

def inloggen():
    inlogGegevens = getGegevens('gegevens')
    while True:
        inputGebruikerNaam = input('Gebruikersnaam: ')
        inputWachtwoord = input('Wachtwoord: ')
        if inputGebruikerNaam in inlogGegevens.keys() and inlogGegevens[inputGebruikerNaam] == inputWachtwoord:
            print('U heeft nu toegang!')
            break
        else:
            print('Verkeerd wachtwoord en/of gebruikersnaam, probeer opnieuw! \n')


def wachtwoordWijzigen():
    inlogGegevens = getGegevens('gegevens')
    while True:
        inputGebruikerNaam = input('Gebruikersnaam: ')
        if inputGebruikerNaam in inlogGegevens.keys():
            inputEmail = getGegevens('email')
            email = inputEmail[inputGebruikerNaam]
            code = getCode(email)
            print('Voer de code in die op uw e-mail verschijnt!')
            inputCode = str(input('Code: '))
            break
        else:
            print('Gebruikersnaam niet correct, probeer opnieuw! \n')
    while True:
        if inputCode == code:
            inputNieuwWachtwoord = input('Nieuw wachtwoord: ')
            inputNieuwWachtwoord2 = input('Herhaal wachtwoord: ')
            if inputNieuwWachtwoord == inputNieuwWachtwoord2:
                print('Uw wachtwoord is aangepast')
                break
            else:
                print('Wachtwoord niet hetzelfde, probeer opnieuw!')
        else:
            print('Code niet correct, probeer opnieuw! \n')
            inputCode = str(input('Code: '))


def getCode(email):
    code = randint(00000000, 99999999)
    code = str(code)
    # try:
    #     server = smtplib.SMTP('smtp.gmail.com:587')
    #     server.ehlo()
    #     server.starttls()
    #     message = 'Code: {}'.format(code)
    #     server.login('randomcodegeneratorkevingoes@gmail.com', 'eaa5932b8')
    #     server.sendmail('randomcodegeneratorkevingoes@gmail.com', 'randomcodegeneratorkevingoes@gmail.com', message)
    #     server.quit()
    #     print('E-mail verzonden')
    # except:
    #     print('E-mail niet verzonden')
    print('U heeft een e-mail gekregen op {}, zoniet wacht 15 seconden!'.format(email))
    time.sleep(15)
    print(code)
    return code


def getGegevens(keuze):
    with open('inloggen.txt', 'r', newline='') as myTextFile:
        inlezen = myTextFile.readlines()
        gegevens = {}
        email = {}
        count = 0
        for item in inlezen:
            gegeven = inlezen[count]
            gegeven = gegeven.replace('\r\n', '')
            gegeven = gegeven.split(';')
            if keuze == 'gegevens':
                gegevens[gegeven[0]] = gegeven[1]
            else:
                email[gegeven[0]] = gegeven[2]
            count += 1
        if keuze == 'gegevens':
            return gegevens
        else:
            return email


while True:
    print('Maak uw keuze:')
    print('1. Inloggen')
    print('2. Wachtwoord wijzigen')
    inputKeuze = input('Keuze: ')
    if inputKeuze == '1':
        inloggen()
        break
    elif inputKeuze == '2':
        wachtwoordWijzigen()
        break
    else:
        email = 'email'
        print(getCode(email))
        break
        # print('Keuze niet beschikbaar, probeer opnieuw')

