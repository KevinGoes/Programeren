invoer = open('kaartnummers.txt', 'r')
aantalRegels = invoer.readlines()
invoer.close()

invoer = open('kaartnummers.txt', 'r')

for gegevens in aantalRegels:
    x = invoer.read(6)
    y = invoer.read(2)
    z = invoer.readline()
    print(z + ' heeft kaartnummer: ' + x)

invoer.close()
