import csv

def consultar_arquivo_csv(filepath):
    """
    :param filepath: caminho do arquivo CSV
    """
    try:
        with open(filepath, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")