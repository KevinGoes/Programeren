def langGenoeg(lengte):
    if lengte >= 120:
        return "Je bent lang genoeg voor de attractie"
    else:
        return "Sorry, je bent te klein"


lengte = int(input("Hoe lang ben je? "))
x = langGenoeg(lengte)
print(x)