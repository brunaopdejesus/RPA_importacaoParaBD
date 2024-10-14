import sqlite3
import pandas as pd

# Passo 1: Leitura do arquivo CSV
csv_file = 'vagas.csv'  # Substitua pelo nome real do seu arquivo CSV
try:
    df = pd.read_csv(csv_file)
    print("Dados lidos com sucesso:")
    print(df.head())  # Exibe as primeiras linhas do DataFrame
except FileNotFoundError:
    print("Arquivo CSV não encontrado. Verifique o caminho e o nome do arquivo.")
    exit()
except Exception as e:
    print(f"Ocorreu um erro ao ler o CSV: {e}")
    exit()

# Verifica se o DataFrame não está vazio
if df.empty:
    print("O DataFrame está vazio. Nenhum dado para inserir.")
    exit()

# Passo 2: Criação do banco de dados SQLite
db_file = 'vagas.db'  # Nome do banco de dados
with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor()

    # Passo 3: Criação da tabela de vagas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vagas (
            id_vaga INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            empresa TEXT NOT NULL,
            localizacao TEXT NOT NULL,
            data_publicacao TEXT NOT NULL,
            faixa_salarial TEXT,
            url_vaga TEXT
        )
    ''')
    print("Tabela 'vagas' criada com sucesso ou já existe.")

    # Passo 4: Inserção dos dados do CSV no banco de dados
    for _, row in df.iterrows():
        try:
            cursor.execute('''
                INSERT INTO vagas (titulo, empresa, localizacao, data_publicacao, faixa_salarial, url_vaga)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (row['Título'], row['Empresa'], row['Localização'], row['Data de Publicação'], row['Faixa Salarial'], row['URL da Vaga']))
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

    # Confirma e conta os registros inseridos
    cursor.execute("SELECT COUNT(*) FROM vagas")
    count = cursor.fetchone()[0]
    print(f"Número de registros inseridos: {count}")

print("Banco de dados criado com sucesso!")
