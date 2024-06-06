from consultarArquivoCSV import consultar_arquivo_csv

def consultar_dados():
    consultaAberta = True

    while consultaAberta:
        print()
        print("Selecione o arquivo que deseja consultar: ")
        print("1 - Produção de Plástico Global")
        print("2 - Participação Despejo Resíduo Plástico")
        print("3 - Destino Plástico")
        print("4 - Desperdício Plástico Per Capita")
        print("5 - Poluição Água Cidades")
        print("0 - Voltar")
        print()

        escolha = int(input("Opção: "))
        match escolha:
            case 1:
                filepath = "1- producao-de-plastico-global.csv"
                consultar_arquivo_csv(filepath)
            case 2:
                filepath = "2- participacao-despejo-residuo-plastico.csv"
                consultar_arquivo_csv(filepath)
            case 3:
                filepath = "3- destino-plastico.csv"
                consultar_arquivo_csv(filepath)
            case 4:
                filepath = "4- desperdicio-plastico-per-capita.csv"
                consultar_arquivo_csv(filepath)
            case 5:
                filepath = "5- poluicao-agua-cidades.csv"
                consultar_arquivo_csv(filepath)
            case 0:
                consultaAberta = False
            case _:
                print('Opção inválida.')
