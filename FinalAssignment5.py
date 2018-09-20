kilometer = int(input("Hoeveel kilometer moet u reizen? "))
leeftijd = int(input("Hoe oud bent u? "))
tijdWeek = input("Reist u in het weekend? 'ja' of 'nee' ")

if kilometer > 50:
    standaardtarief = (15+0.60*kilometer)
    if tijdWeek == 'ja':
        if leeftijd <= 12 or leeftijd >= 65:
            print("U krijgt 35% korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief*0.65, 2))
        else:
            print("U krijgt 40% korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief*0.60, 2))
    else:
        if leeftijd <= 12 or leeftijd >= 65:
            print("U krijgt 30% korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief*0.7, 2))
        else:
            print("Helaas, u krijgt geen korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief, 2))
else:
    standaardtarief = (0.80*kilometer)
    if tijdWeek == 'ja':
        if leeftijd <= 12 or leeftijd >= 65:
            print("U krijgt 35% korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief * 0.65, 2))
        else:
            print("U krijgt 40% korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief * 0.60, 2))
    else:
        if leeftijd <= 12 or leeftijd >= 65:
            print("U krijgt 30% korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief * 0.7, 2))
        else:
            print("Helaas, u krijgt geen korting, daarmee komt u uit op een bedrag van: ")
            print(round(standaardtarief, 2))
