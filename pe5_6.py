s = "Guido van Rossum heeft programmeertaal Python bedacht."

for klinker in s:
    if klinker in ("AEOIUaeoiu"):
        print(klinker)
