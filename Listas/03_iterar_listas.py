#iterar listas
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

#função enumerate
for indice, carro in enumerate(carros):
    print(f"{indice}, {carro}")