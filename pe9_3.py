cijfers = {'Kever': 7.8, 'Clarinetta': 2.7, 'Karin': 6.0, 'Rebecca': 9.1, 'Alex': 10.0, 'Zwarissa': 6.7, 'Swanetta': 9.5, 'Kroketta': 8.9}

for getal in cijfers:
    cijfer = cijfers[getal]
    if cijfer > 9.0:
        print(getal, end=': ')
        print(cijfer)
