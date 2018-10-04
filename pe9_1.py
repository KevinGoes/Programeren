def sum():
    total = 0
    aantalKeer = 0
    while True:
        nextInt = input('Geef een getal: ')
        if nextInt == '0':
            break
        else:
            total += int(nextInt)
            aantalKeer += 1
    return total, aantalKeer


x, y = sum()
print('Er zijn', y, 'getallen ingevoer, de som is:', x)