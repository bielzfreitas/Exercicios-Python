# Criando dicionario de dados
usuarios = {}

# Preenchendo o dicionario
# Criando uma list apara armazenar os dados
# Nome / Data do último acesso / ùltima estação utilizada
usuarios = {
    "Chaves":["Chaves Silva","17/06/1975","Recep_01"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_02"],
    "Quico":["Enrico Flores","03/06/1976","Raiox_03"]
    }

# Adicionando de maneira singular
usuarios["Florinda"]=["Florinda Flores", "26/11/2017", "Recep_01"]
usuarios["Florinda"]=["Florinda Flores", "26/11/2016", "Recep_01"]

# Retornando dados de um objeto da lista
print(usuarios)
print("########====########")
print("Dados: ", usuarios.get("Chaves"))