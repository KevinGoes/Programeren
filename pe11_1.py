bedrag = 4356
invoer = input('Met hoeveel personen bent u: ')
while True:
    if int(invoer) < 0:
        print('Aantal personen is negatief!')
        break
    try:
        print(bedrag / int(invoer), 'Euro')
        break
    except ValueError:
        print('Vul een nummer(van aantal personen) in!')
        break
    except ZeroDivisionError:
        print('Aantal personen is gelijk aan 0')
        break
    except:
        print('Andere fout!')
        break


