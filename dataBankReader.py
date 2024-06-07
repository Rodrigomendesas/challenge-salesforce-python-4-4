from databaseConnection import database_connection
import oracledb

def consultar_banco_de_dados():
    print()
    print("1 - Consultar nomes das tabelas")
    print("2 - Consultar tabela específica por nome")
    print("0 - Voltar")

    escolha = int(input("Opção: "))
    match escolha:
        case 1:
            table_names = []
            try:
                conn = database_connection()
                cursor = conn.cursor()
                cursor.execute("SELECT table_name FROM user_tables")
                table_names = [row[0] for row in cursor.fetchall()]
            except oracledb.DatabaseError as e:
                error, = e.args
                print(f"Error retrieving table names: {error.message}")
            finally:
                cursor.close()
                conn.close()
            print(table_names)
        case 2:
            table_name = input("Digite o nome da tabela que deseja consultar: ")
            try:
                conn = database_connection()
                cursor = conn.cursor()
                consulta = "SELECT * FROM {table_name}"
                cursor.execute(consulta)
                lista_dados = cursor.fetchall()
                if len(lista_dados) == 0:
                    print("Essa tabela está vazia")
                else:
                    for item in lista_dados:
                        print(item)
            except Exception as erro:
                print("Erro: " + erro)

