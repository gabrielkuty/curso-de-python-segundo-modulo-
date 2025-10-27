pessoa = {"nome": "Guilherme", "idade": 28}
pessoa = dict(nome = "Guilherme", idade = 28)
pessoa["telefone"] = "3341-8366"

print(pessoa["nome"])
print(pessoa["telefone"])
print(pessoa["idade"])
print(pessoa)

pessoa["nome"] = "Maria"
pessoa["idade"] = 28
pessoa["telefone"] = "999281437"

print(pessoa)

#dicionarios aninhados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-9876"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-5432"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-9843"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3323-8843"}
}
print(contatos["giovanna@gmail.com"]["telefone"])

for chave in contatos:
    print(chave, contatos[chave])

for chave, valor in contatos.items():
    print(chave, contatos[chave])