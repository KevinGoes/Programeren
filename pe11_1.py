def invoer():
    invoer = input('Met hoeveel personen bent u? ')
    if invoer < 0:
        raise ValueError('Aantal personen is kleiner dan 0')


bedrag = 4356

try:
    print(int(bedrag) / int(invoer()))
except ZeroDivisionError:
    print('Aantal personen is gelijk aan 0')
except ValueError:
    print('Aantal personen is kleiner dan 0')
except TypeError:
    print('Vul een nummer(van aantal personen) in!')
except:
    print('Andere fout!')
