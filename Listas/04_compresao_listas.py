#filtro 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []
quadrado = []

for numero in numeros:
    if numero % 2 == 0 :
        pares.append(numero)

print(pares[::])

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)
# filtro 2

pares = [numero for numero in numeros if numero % 2 == 0]
print(pares[::])

quadrado = [numero ** 2 for numero in numeros ]
print(quadrado)