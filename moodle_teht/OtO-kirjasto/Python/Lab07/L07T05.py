class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    
car1 = Car("Skooda", "Octavia", 3000)
car2 = Car("Audi", "A4", 4000)
car3 = Car("Volvo", "V70", 5000)

sum = 0
for car in [car1, car2, car3]:
    sum += car.price
    print(car.brand, car.model, car.price)

print("Autojen hinta yhteensä:", sum)
