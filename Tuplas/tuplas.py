frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil", )

frutas[0]
frutas[2]

frutas[-1]
frutas[-2]

matriz = (
    (1, "a", 2),
    ("b", 3, 4)
    (6, 5, "c")
)
matriz[0]
matriz[0][0]
matriz[0][-1]
matriz[-1][-1]
# fatiamento igual em lista


carros = ("gol", "celta", "palio")

for indice, carro in enumerate(carros):
    print(f"{indice}, {carro}")

