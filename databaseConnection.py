import oracledb
import pwinput

def database_connection():

    login = input('Usuário: ')
    senha = pwinput.pwinput('Senha: ')
    
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

