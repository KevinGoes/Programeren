while True:
    invoer = input('Geef een string van 4 letters: ')
    if len(invoer) == 4:
        break
    else:
        print(invoer, 'heeft', len(invoer), 'letters.')
print('Inlezen van correcte string: ', invoer, 'is geslaagd.')
