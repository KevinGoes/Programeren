def rng(numberList):
    return abs(max(numberList) - min(numberList))


x = rng([4, 0, 1, -2]) * 2
print(x)