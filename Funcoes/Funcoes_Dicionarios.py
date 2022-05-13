# F1 -> ao usuário e retorna a resposta do usuário
# F2 -> receberá um dicionário e insere um objeto dentro do dic

# Pesquisar -> recebe o dic e a chave, preenche uma lista
# com o resultado da pesquisa (get()), verifica se não está
# vazio ( != diferente ). Caso seja true, exibe os dados.
# ---- % ----
# Primeira posição (zero) -> nome do usuário
# Segunda posiação (um) -> última data de acesso
# Terceira posição (dois) -> última estação acessada
# ---- % ----
# Excluir -> recebe o dic de onde o objeto será excluído
# e a chave do objeto que deseja excluir.
# Antes da exclusão, deve verificar se a chave existe (get())
# se será retornado algo diferente de vazio
# Caso seja true, invoca o comando "del"
# ---- % ----
# Listar -> precisa apenas do dic que contém os dados a exibir
# montar um foreach utilizando dois valores (chave e valor) podendo
# dar uma saída mais "clean"
# ---- % ----


def perguntar():
    resposta = input("O que deseja realizar?" +
            "<I> - Para Inserir um usuário" +
            "<P> - Para Pesquisar um usuário" +
            "<E> - Para Excluir um usuário" +
            "<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                input("Digite a última data de acesso: "),
                input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista != None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!= None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto...:")
        print("Login....: ", chave)
        print("Dados....: ", valor)