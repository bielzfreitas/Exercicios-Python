# Import das bibliotecas
import os
from ftplib import *

# Definindo o "ftp" para conexão -> "ftp.ibge.gov.br"
ftp_ativo = False

# Exibindo mensagens de boas-vindas
ftp = FTP(input("Digite o FTP que se deseja conectar: "))
print(ftp.getwelcome())

# Solicitando usuário e senha -> pode deixar os dois vazios para "ibge"
usuario = input("Digite o usuario: ")
senha = input("Digite a senha: ")

# Estabelece o login e mostra mensagem de conexão estabelecida
ftp.login(usuario, senha)
print("Conexão bem sucedida. Diretório atual de trabalho: ", ftp.pwd(), "")

# Variável "menu" criada
menu = "1"

# Lista de diretórios -> exibindo arquivos e diretórios
# Após -> volta ao menu
while menu == "1" or menu == "2" or menu == "3":
    menu = input("Escolha a opção desejada: "
                 "< 1 > - para Listar arquivos"
                 "< 2 > - para definir um diretório"
                 "< 3 > - para baixar um arquivo: ")
    if menu == "1":
        print(ftp.dir())
    
    # Caso seja "2", muda o diretório de acordo com que o usuário digitar
    # Digitar "seculoxx"
    elif menu == "2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print("Diretório corrente é: ", ftp.pwd())
    
    # Ao digitar "3", exibi se usuário deseja baixar
    # Digitar "b"
    elif menu == "3":
        tipo = input("Digite <B> para arquivo binário ou "
                     "qualquer outra letra para arquivo ASCII: ").upper()
        
        # Solicita o nome do arquivo destino
        # Digitar "zipado.zip"
        # Escolher o arquivo "representacao_politica.zip"
        # Escolher opção 3 para baixar
        # Próxima pergunta -> digitar qualquer letra DIFERENTE de "b"
        if tipo == "B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Arquivo de origem:"), escreverLinha)
        
        print("Arquivo baixado com sucesso! ")
ftp.quit()
