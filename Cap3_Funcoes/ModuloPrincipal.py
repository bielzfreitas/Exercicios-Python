# from -> recebe local fisico no qual se encontram
#         as funcoes que se deseja importar
# import -> defini quais funcioes deseja importar
# "*" asterisco -> importa TODAS as funcoes

from Cap3_Funcoes.IdentificacaoDeFuncoes import *

minhaLista = []

print("Preenchendo")
preencherInventario(minhaLista)

print("Exibindo")
exibirInventario(minhaLista)

print("Pesquisando")
localizarPorNome(minhaLista)

print("Alterando")
depreciarPorNome(minhaLista, 20)

print("Excluindo")
print(excluirPorSerial(minhaLista))
exibirInventario(minhaLista)

print("Resumindo")
resumirValores(minhaLista)