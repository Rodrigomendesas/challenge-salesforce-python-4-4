import csv
import oracledb

def inserir_dados_no_banco_de_dados(filepath, table_name):
    
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
        cursor = None
    
    if cursor is not None:
        try:        
            with open(filepath, mode='r', newline='') as file:
                csv_reader = csv.reader(file)
                headers = next(csv_reader)
                placeholders = ", ".join([":" + str(i + 1) for i in range(len(headers))])
                insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"

                for row in csv_reader:
                    cursor.execute(insert_query, row)
            
            conn.commit()
            print("Dados inseridos")
        except FileNotFoundError:
            print(f"File {filepath} not found.")
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Erro ao inserir dados no banco de dados: {error.message}")
        except Exception as e:
            print(f"Erro: {e}")
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()
