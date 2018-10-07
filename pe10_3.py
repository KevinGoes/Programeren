def code(invoerstring):
    zin  = invoerstring
    zin = list(zin)
    zinASCII = []
    for letter in range(len(zin)):
        ASCIINummer = ord(zin[letter]) + 3
        ASCIINummer = chr(ASCIINummer)
        zinASCII.append(ASCIINummer)
        print(zinASCII[letter], end='')
    print('')


print(code(input('Voer gebruiker+beginstation+eindstation in: ')))
