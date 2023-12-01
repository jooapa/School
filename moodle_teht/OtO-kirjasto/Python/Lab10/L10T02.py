
while True:
    try:
        syntymavuosi = int(input("Kerro syntymävuotesi: "))

        break
    except ValueError:
        print("syntymävuosi pitäisi olla")

if syntymavuosi % 4 == 0:
    print(syntymavuosi, "is a leap year!")
else:
    print(syntymavuosi, "is not a leap year!")