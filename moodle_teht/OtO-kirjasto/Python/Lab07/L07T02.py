class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Nimi {self.name}, {self.age} vuotta"
    

jooa = Human("Jooa", 17)
batman = Human("Bruce", 29)

print(jooa)
print(batman)