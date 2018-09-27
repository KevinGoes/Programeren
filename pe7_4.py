import datetime
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y, %I:%M:%S")
laatsteBinnenkomer = ' '
binnenKomer = input("Hoe heet je? ")

while binnenKomer != laatsteBinnenkomer:
    invoer = open('hardlopers.txt', 'a')
    invoer.write(s, ' ', binnenKomer, '\n')
    laatsteBinnenkomer = binnenKomer
    invoer.close()
    binnenKomer = input("Hoe heet je? ")