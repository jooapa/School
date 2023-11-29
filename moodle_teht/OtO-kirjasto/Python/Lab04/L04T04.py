
while True:
  luku = input("Anna luku väliltä 1-10: ")
  try:
    luku = int(luku)
    if luku < 1 or luku > 10:
      print("Luku ei ole väliltä 1-10!")
    else:
      for i in range(luku):
        print("luvun", i+1, "neliö on", (i+1)**2)
  except ValueError:
    print("Virheellinen syöte!")


