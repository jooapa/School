autot = {
    "ABC-123": "Volkswagen",
    "DEF-456": "Toyota",
    "GHI-789": "Audi",
    "JKL-012": "BMW",
    "MNO-345": "Fiat",
    "PQR-678": "Ford",
}

print("Autot aakkosjärjestyksessä rekisterinumeron mukaan:")
for rekisterinumero in sorted(autot):
    print(
        f"Rekisterinumero: {rekisterinumero}, Merkki: {autot[rekisterinumero]}")
