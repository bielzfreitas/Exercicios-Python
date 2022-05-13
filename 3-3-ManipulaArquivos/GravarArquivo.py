# Utilização da Função Open
# Arquivo aberto para escrita
# Write() -> permite passar conteúdo para dentro do arquivo
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "w") as arquivo:
    arquivo.write("Continuação do texto.")