invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
invoerLijst = invoer.split('-')
gesorteerd = (invoerLijst.sort())
tijdelijkeLijst = []
for i in range(len(invoerLijst)):
    tmp = int(invoerLijst[i])
    tijdelijkeLijst.append(tmp)

print(tijdelijkeLijst)
print("Grootste getal:", max(tijdelijkeLijst), "en Kleinste getal:", min(tijdelijkeLijst))
print("Aantal getallen:", len(tijdelijkeLijst), "en de Som van de getallen:", sum(tijdelijkeLijst))
print("Gemiddelde", sum(tijdelijkeLijst) / len(tijdelijkeLijst))




