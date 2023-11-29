class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color
      
    def miau(self):
        print(f"{self.name} says: Meoooooow!")

    def __str__(self):
        return f"{self.name}, color {self.color}"
    
kit = Cat("Kit", "Black")
kat = Cat("Kat", "White")

print(kit)
print(kat)
kit.miau()
kat.miau()