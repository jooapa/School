pisteet = -1

while pisteet < 0 or pisteet > 12:
    pisteet = int(input("Pisteet: "))

    if pisteet >= 0 and pisteet <= 1:
        arvosana = 0
    elif pisteet >= 2 and pisteet <= 3:
        arvosana = 1
    elif pisteet >= 4 and pisteet <= 5:
        arvosana = 2
    elif pisteet >= 6 and pisteet <= 7:
        arvosana = 3
    elif pisteet >= 8 and pisteet <= 9:
        arvosana = 4
    elif pisteet >= 10 and pisteet <= 12:
        arvosana = 5
    else:
        print("Virheellinen pisteiden määrä!")
        continue

print("Arvosana:", arvosana)
