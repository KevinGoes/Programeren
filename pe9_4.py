def ticker():
    dict = {}
    fileInvoer = open('ticker.txt', 'r')
    aantalRegels = fileInvoer.readlines()
    fileInvoer.seek(0)
    for regel in range(len(aantalRegels)):
        tmp = fileInvoer.readline()
        tmp = tmp.replace('\n', '')
        tmp = tmp.split(':')
        dict[tmp[0]] = tmp[1]
    fileInvoer.close()
    return dict


dict = ticker()
invoerCompany = input('Enter Company Name: ')
print('Ticker Symbol = {} \n'.format(dict[invoerCompany]))

invoerAfkorting = input('Enter Ticker Symbol: ')
for regel in dict:
    if dict[regel] == invoerAfkorting:
        print('Company Name = {}'.format(regel))

