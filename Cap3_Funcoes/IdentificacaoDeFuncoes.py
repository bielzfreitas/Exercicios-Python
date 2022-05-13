# criando funções

# função que preenche o inventário
# -> recebe parametro que é a lista na qual o
#    módulo principal armazenará os itens do inv

def preencherInventario(lista):
  resp = "S"
  
  while resp == "S":
    equipamento = [input("Equipamento: "),
              float(input("Valor: ")),
              int(input("Número Serial: ")),
              input("Departamento: ")]
    
    lista.append(equipamento)
    resp = input("Digite S para continuar: ").upper()

# recebe a lista por parametro e executa o laço
# for para exibir os dados da lista recebida

def preencherInventario(lista):
    resp = "S"

    while resp == "S":
        equipamento = [input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Número Serial: ")),
        input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite S para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

# criando funções

# recebe a lista, solicita o nome, localiza o nome
# do produto na lista e exibe ao encontrar
def localizarPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor...: ", elemento[1])
            print("Serial..: ", elemento[2])

# Parametro1 -> lista na qual os equipamentos que
# sofrerao a depreciacao
# Paramento2 -> porcentagem que se deseja depreciar
def depreciarPorNome(lista, porc):
    depreciacao = input("Digite o nome do equipamento que será depreciado: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1-porc/100)
            print("Novo valor: ", elemento[1])

# retorna uma string
def excluirPorSerial(lista):
    serial = int(input("Digite o serial do equipamento que será excluido: "))
    for elemento in lista:
        if elemento[2] == serial:
            lista.remove(elemento)
    return "Itens excluídos."

# Funcao1 -> somar()
# Funcao2 -> exibirMaiorValor()
# Funcao3 -> exibirMenorValor()
def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O valor total de equipamentos é de: ", sum(valores))