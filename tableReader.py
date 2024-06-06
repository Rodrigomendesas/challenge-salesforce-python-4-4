from databaseConnection import database_connection
from consultarDados import consultar_dados
from inderirDadosNoBancoDeDados import inserir_dados_no_banco_de_dados

conexao = True
database_connection()

def acessar_banco():
    database_connection()

    InsercaoAberta = True

    while InsercaoAberta:
        print()
        print("Selecione o arquivo que deseja inserir no banco de dados: ")
        print("1 - Produção de Plástico Global")
        print("2 - Poluição Água Cidades")
        print("0 - Voltar")
        print()

        escolha = int(input("Opção: "))
        match escolha:
            case 1:
                filepath = "1- producao-de-plastico-global.csv"
                inserir_dados_no_banco_de_dados(filepath)
            case 2:
                filepath = "5- poluicao-agua-cidades.csv"
                inserir_dados_no_banco_de_dados(filepath)
            case 0:
                InsercaoAberta = False
            case _:
                print('Opção inválida.')

while conexao:
    print()
    print("1 - Consultar dados")
    print("2 - Inserir dados no banco de dados")
    print("0 - Sair")
    escolha = int(input("Opção: "))
    match escolha:
        case 1:
            consultar_dados()
        case 2:
            acessar_banco()
        case 0:
            print('Programa finalizado.')
            conexao = False
        case _:
            print('Opção inválida.')

