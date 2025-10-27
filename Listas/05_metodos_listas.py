# append

lista = []

lista.append(1)
lista.append("Python")
lista.append([40, 30, 20])

print(lista)
#copy
l2 = lista.copy()
#clear
lista.clear()

print(lista)
print(l2)

#count
cores = ["vermelho", "azul", "verde", "azul"]
print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#extend
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp", "js"])
print(linguagens)

#index
print(linguagens.index("java"))
print(linguagens.index("python"))

#pop
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop())
print(linguagens.pop(0))
print(linguagens)
#remove
linguagens = ["python", "js", "c"]

print(linguagens)

linguagens.extend(["java", "csharp", "js"])

linguagens.remove("c")

#reverse
linguagens.reverse()
print(linguagens)

#sort

print(linguagens.sort())
print(linguagens.sort(reverse = True))
print(linguagens.sort(key=lambda x: len(x)))
print(linguagens.sort(key=lambda x: len(x), reverse=True))

#len
linguagens = ["python", "js", "c"]
linguagens.extend(["java", "csharp", "js"])

len(linguagens)