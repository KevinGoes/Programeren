def convert(tempC):
    tempF = tempC * 1.8 + 32
    return tempF

def table():
    print("F \t \t C")
    for i in range(-30, 41, 10):
        uitkomst = i * 1.8 + 32
        print(uitkomst, "\t", float(i))


print(convert(25))
print("\n")
print(table())


