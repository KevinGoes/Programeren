def sum():
    total = 0
    while True:
        nextInt = input('next int: ')
        if nextInt == 'quit':
            break
        else:
            total += int(nextInt)
    return total


print(sum())
