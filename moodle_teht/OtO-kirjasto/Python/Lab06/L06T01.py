def showtime(sec):
    hours = sec // 3600
    minutes = (sec - hours * 3600) // 60
    seconds = sec - hours * 3600 - minutes * 60
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}") # f tarvitaan, jotta :02d toimii, ja :02d, jotta saadaan 0 eteen

print(showtime(500))
print(showtime(10000))
print(showtime(121000))
