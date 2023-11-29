def celToFah(celsius):
    return celsius * 9 / 5 + 32

def fahToCel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(celToFah(10.0))
print(fahToCel(38.0))