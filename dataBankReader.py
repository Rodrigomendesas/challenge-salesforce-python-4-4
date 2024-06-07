from databaseConnection import database_connection
import oracledb

def consultar_banco_de_dados():
    consultaBancoDeDados = True
    while consultaBancoDeDados:
        print()
        print("1 - Consultar nomes das tabelas")
        print("2 - Consultar tabela específica por nome")
        print("0 - Voltar")

        escolha = int(input("Opção: "))
        match escolha:
            case 1:
                table_names = []
                conn = None
                cursor = None
                try:
                    login = "RM552602"
                    senha = "120203"
                    conn = oracledb.connect(user=login,
                        password=senha,
                        host="oracle.fiap.com.br",
                        port=1521,
                        service_name="ORCL")
                    cursor = conn.cursor()
                    cursor.execute("SELECT table_name FROM user_tables")
                    table_names = [row[0] for row in cursor.fetchall()]
                except oracledb.DatabaseError as e:
                    error, = e.args
                    print(f"Erro ao buscar nomes das tabelas: {error.message}")
                finally:
                    if cursor is not None:
                        cursor.close()
                    if conn is not None:
                        conn.close()
                print(table_names)
            case 2:
                table_name = input("Digite o nome da tabela que deseja consultar: ")
                conn = None
                cursor = None
                try:
                    login = "RM552602"
                    senha = "120203"
                    conn = oracledb.connect(
                        user=login,
                        password=senha,
                        host="oracle.fiap.com.br",
                        port=1521,
                        service_name="ORCL"
                    )
                    cursor = conn.cursor()
                    consulta = f"SELECT * FROM {table_name}"
                    cursor.execute(consulta)
                    lista_dados = cursor.fetchall()
                    if len(lista_dados) == 0:
                        print("Essa tabela está vazia")
                    else:
                        for item in lista_dados:
                            print(item)
                except Exception as erro:
                    print("Erro: " + erro)
            case 0:
                print("Voltando...")
                consultaBancoDeDados = False
