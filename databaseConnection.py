import oracledb

def database_connection():

    login = "RM552602"
    senha = 120203
    
    try:
        conn = oracledb.connect(user=login,
        password=senha,
        host="oracle.fiap.com.br",
        port=1521,
        service_name="ORCL")
        cursor = conn.cursor()
    except Exception as erro:
        print(f"Erro: {erro}") 
        conexao = False 
    else:
        conexao = True 

