def wijzig(lijst):
    for letter in range(len(lijst)):
        lijst.pop()
    lijst.append('d')
    lijst.append('e')
    lijst.append('f')


lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)

