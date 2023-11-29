import datetime

nimi = input("Anna etunimesi: ")
vuosi = int(input("Anna syntymävuotesi: "))
today = datetime.date.today()

print("Hei " + nimi + ", olet", today.year - int(vuosi), "vuotta.")
