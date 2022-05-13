# Criar variavel "acao" que recebe letras "L" ou "D"
# Perguntar ao usuário  
# Avaliar se o valor é igual a "L" ou "D"
# Perguntar ao usuário o que deseja realizar

import serial

conexao = ""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    
    except serial.SerialException:
        pass

if conexao != "":
    acao = input("Digite: <L> para Ligar <D> para Desligar: ").upper()
    while acao == "L" or acao == "D":
        if acao == "L":
            conexao.write(b'1')
        
        else:
            conexao.write(b'0')
        acao = input("Digite: <L> para Ligar <D> para Desligar: ").upper()
    
    conexao.close()
    print("Conexao encerrada")

else:
    print("Sem portas disponíveis")
