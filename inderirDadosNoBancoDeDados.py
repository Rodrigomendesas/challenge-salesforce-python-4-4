import csv
import oracledb
from databaseConnection import database_connection

def inserir_dados_no_banco_de_dados(filepath, table_name):
    
    conn = database_connection()
    cursor = conn.cursor()
    
    try:
        
        with open(filepath, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            placeholders = ", ".join([":" + str(i + 1) for i in range(len(headers))])
            insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"

            for row in csv_reader:
                cursor.execute(insert_query, row)
        
        conn.commit()
        print("Data successfully inserted into the database.")
    except FileNotFoundError:
        print(f"File {filepath} not found.")
    except oracledb.DatabaseError as e:
        error, = e.args
        print(f"Error inserting data into Oracle database: {error.message}")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        conn.close()
