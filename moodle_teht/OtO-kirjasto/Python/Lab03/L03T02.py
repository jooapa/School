num1 = int(input("Anna kokonaisluku: "))
num2 = int(input("Anna toinen kokonaisluku: "))
num3 = int(input("Anna kolmas kokonaisluku: "))

if num1 > num2 and num1 > num3:
    print("Suurin:", num1)
elif num2 > num1 and num2 > num3:
  print("Suurin:", num2)
elif num3 > num1 and num3 > num2:
  print("Suurin:", num3)
else:
  print("Luvut ovat yhtä suuret!")  