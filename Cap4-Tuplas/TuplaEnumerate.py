# Utilização da Tupla Enumerate
# Quando precisa numerar cada compenente da lista a fim
# de garantir que cada elemento dela poderá ser utilizado
# como dado chave de um dicionário

# Dicionário criado
# E-mail do usuáro sendo chave do dicionário
# Outros dados (nome e nível) sendo lista

usuarios = {}
resp = "S"
emails = []
while resp == "S":
    emails.append(input("Digite um e-mail: ").lower())
    resp = input("Digite <S> para continuar: ").upper()

# E-mails numa lista e gerando tuplas por número sequencial
# Enumerando cada item da lista e gerando uma tupla com cada elemtno
# Utilizando o laço "for" atrelado ao tamanho da tupla
# Quantidade de e-mails que foram armazenados
tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]] = [input("Digite o nome: "), input("Digite o nível: ")]

# Exibindo dados do dicionário
# String é uma lista com característica de tupla -> SIMBIOSE
for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])