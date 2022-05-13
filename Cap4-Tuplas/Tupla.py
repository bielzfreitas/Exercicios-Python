# Dicionário ips
# Variável resp para controlar o laço
# Preenche o dicionário dentro do laço
# Na chave do dicionário, insere dois valores


ips = {}
resp = "S"
while resp == "S":
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))] = input("Nome da máquina: ")
    resp = input("Digite <S> para continuar: ").upper()

# Aproveitando os dados da chave no formato de tupla
# Saída apresentando os IPs
print("Exibindo ip´s: ")
for ip in ips.keys():
    print(ip[0] + "." + ip[1])

# Solicita a segunda prte do IP ao usuário
# Endereço da máquina
# Exibi os nomes das máquinas
print("Exibindo máquinas com o mesmo endereço: ")
pesquisa = input("Digite os dois últimos octetos: ")
for ip, nome in ips.items():
    print("Máquinas no mesmo endereço (redes diferentes)")
    if(ip[1] == pesquisa):
        print(nome)

# Estações que compoem a rede
print("Exibindo as máquinas que compõem uma mesma rede: ")
rede = input("Digite os dois primeiros octetos: ")
for ip, nome in ips.items():
    if(ip[0] == rede):
        print(nome)

# Solicitado os dois primeiros octetos para o usuário
# Montado o laço "for" recebendo os dois valores do dicionário (chave e dado)
# Chave sendo uma tupla formada por dois valores
# Primeiro valor usado para comparar com o contrúdo da variável "rede"
# Caso sejam iguais, exibi os nomes das estações que compõem ou que estão "penduradas" na rede