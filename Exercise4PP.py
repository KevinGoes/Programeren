def BMI(gewicht, lengte):
    bmiWaarde = (gewicht * 703) / lengte**2
    return bmiWaarde


gewicht = int(input("Hoeveel weeg je? (pounds) "))
lengte = int(input("Hoe lang ben je? (inches) "))
print(round(BMI(gewicht, lengte), 2))

if BMI(gewicht, lengte) < 18.5:
    print('Underweight')
elif BMI(gewicht, lengte) < 25.0:
    print('Normal Weight')
else:
    print('Overweight')