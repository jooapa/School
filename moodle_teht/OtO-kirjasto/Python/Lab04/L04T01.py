luku = int(input("Montako lukua: "))

sum = 0
num = 10

for i in range(luku):
    if i != 0:
        sum += num
    
    print(str(i) + ". luku:", sum)
    