#declarando função
def exibir_mensagem():
    print('Olá mundo!')

def exibir_mensagem_2(nome):
    print(f"seja bem vindo {nome}!")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"seja bem vindo {nome}!")

print(exibir_mensagem())
print(exibir_mensagem_2(nome = "Guilherme"))
print(exibir_mensagem_3())
print(exibir_mensagem_3(nome = "Chappie"))

# retornando valores
def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor

total = calcular_total([10, 20, 34])
antsuc = retorna_antecessor_e_sucessor(10)

print(total)
print(antsuc)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso ! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca = "Fiat", modelo = "Palio", ano = 1999, placa = "ABC-1234")
