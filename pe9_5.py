def namen():
    namen = []
    while True:
        invoer = input('Volgende Naam: ')
        if invoer == '':
            break
        else:
            namen.append(invoer)
            aantal = {}
            for naam in namen:
                if naam in aantal:
                    aantal[naam] += 1
                else:
                    aantal[naam] = 1
            break
    return aantal


print(namen())
