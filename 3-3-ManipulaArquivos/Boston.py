# Qual o total de voos internacionais que partiram do aeroporto de Logan em 2014?
# Quando (mês/ano) ocorreu o maior trânsito de passageiros no aeroporto de Logan?
# Qual o total de passageiros que passaram pelo aeroporto de Logan, no ano especificado pelo usuário?
# Qual o mês que possui maior média da diária de um hotel, com base no ano especificado pelo usuário?

# Arquivo em modo leitura
# Cria variável para armazenar voos
with open("economic-indicators.csv","r") as boston:
    
    total_voos = 0
    maior = 0
    total_passageiros = 0
    maior_media_diaria = 0
    ano_usuario = input("Qual ano deseja pesquisar? ")
    
    for linha in boston.readlines()[1:-1]:
        lista = linha.split(",")
        total_voos = total_voos + float(lista[3])
        
        if float(lista[2]) > float(maior):
            maior = lista[2]
            ano = lista[0]
            mes = lista[1]
        
        if ano_usuario == lista[0]:
            total_passageiros = total_passageiros + float(lista[2])
            
            if float(lista[5]) > float(maior_media_diaria):
                maior_media_diaria = lista[5]
                mes_maior_diaria = lista[1]
    
    print("O total de voos é: ", total_voos)
    print("O mês/ano de maior movimento no aeroporto foi: ", str(mes),"/",str(ano))
    print("O total de passageiros do ano ", ano_usuario, "foi de ", total_passageiros)
    print("O mês do ano ", ano_usuario, "com maior média para diária de hotel foi ", mes_maior_diaria)

