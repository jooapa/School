def get_cost(kilometrit, keskiKulutus, litraHinta):
  kmKulutus = (kilometrit * keskiKulutus) / 100
  return str(round(kmKulutus * litraHinta, 2)) + " €"

print(get_cost(100, 7.5,1.88))
print(get_cost(220, 6.9,1.88))
