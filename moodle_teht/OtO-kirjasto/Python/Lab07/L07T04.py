class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
      
phone1 = Mobile("Samsung", "Galaxy", 349)
phone2 = Mobile("Apple", "iPhone 12", 899)

print(phone1.brand, phone1.model, "price:", phone1.price, "€")
print(phone2.brand, phone2.model, "price:", phone2.price, "€")
