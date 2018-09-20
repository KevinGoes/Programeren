kilometer = int(input("Hoeveel kilometer moet u reizen? "))
leeftijd = int(input("Hoe oud bent u? "))
tijdWeek = input("Reist u in het weekend? 'ja' of 'nee' ")

if kilometer > 50:
    standaardtarief = (15+0.60*kilometer)
    if tijdWeek == 'ja':
        if leeftijd <= 12 or leeftijd >= 65:
            print(standaardtarief*0.65)
        else:
            print(standaardtarief*0.60)
    else:
        if leeftijd <= 12 or leeftijd >= 65:
            print(standaardtarief*0.7)
        else:
            print(standaardtarief)
else:
    standaardtarief = (0.80*kilometer)
    if tijdWeek == 'ja':
        if leeftijd <= 12 or leeftijd >= 65:
            print(standaardtarief * 0.65)
        else:
            print(standaardtarief * 0.60)
    else:
        if leeftijd <= 12 or leeftijd >= 65:
            print(standaardtarief * 0.7)
        else:
            print(standaardtarief)

