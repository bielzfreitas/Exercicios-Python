# Importar a biblioteca "serial"
# Criar conexão
# "COM3" -> saída serial que utilziará no Arduino Sketch
# Segundo parâmetro -> indica o "Baud Rate" que é associado à capacidade de transmissão de bits por segundo
# Identificar quando a porta do dispositivo está conectada
# Abrir um "for" caracterizando um laço de repetição de 0 a 10 (representa a porta do Arduino)
# Bloco "try" acompanhado com "except"
# Tenta estabelecer a conexão com a porta serial
# Somente será executado se ocorrer sucesso
# Abandona o laço quando conexão for estabelecida
# Fazer com que o sistema não seja abortado
# Caso conteúdo não seja vazio, irá fechar a conexão
# Caso contrário, exibi a mensagem "Sem portas disponíveis"


import serial

conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")


