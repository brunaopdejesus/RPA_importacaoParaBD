# Projeto de Importação de Vagas para Banco de Dados SQLite

## Integrantes
- Ana Cristina | RM: 99816
- Bruna Oliveira | RM: 99518
- Luiza Gomes | RM: 97797 
- Raphael Papa | RM: 552432

## Descrição do Projeto

Este projeto tem como objetivo ler um dataset de vagas de emprego a partir de um arquivo CSV, processar os dados utilizando o Pandas e inseri-los em um banco de dados SQLite. O projeto faz parte de uma sprint onde os dados extraídos serão formalmente estruturados e armazenados em um banco de dados para facilitar consultas e análises futuras.

A aplicação utiliza Python, SQLite e Pandas para realizar o processo de importação e inserção dos dados.

## Estrutura do Projeto

- `import_vagas.py`: Script principal que realiza a leitura do arquivo CSV, cria a tabela no banco de dados SQLite e insere os dados no banco.
- `vagas.csv`: Arquivo de dados CSV que contém as informações das vagas de emprego. Ele é lido pelo script Python e processado para inserção no banco de dados.
- `vagas.db`: Arquivo do banco de dados SQLite gerado automaticamente após a execução do script. Ele contém a tabela estruturada com os dados das vagas.

## Componentes do Projeto

### 1. **import_vagas.py**

Este é o script Python que executa as seguintes funções principais:

- **Leitura do CSV**: O arquivo CSV é lido utilizando a biblioteca Pandas, que transforma os dados em um DataFrame, permitindo fácil manipulação.
- **Criação do Banco de Dados SQLite**: Utiliza-se o módulo `sqlite3` para conectar e criar o banco de dados `vagas.db`. Caso o arquivo já exista, ele será reutilizado.
- **Criação da Tabela**: Uma tabela chamada `vagas` é criada, contendo as colunas que refletem os dados do CSV: `id_vaga`, `titulo`, `empresa`, `localizacao`, `data_publicacao`, `faixa_salarial`, e `url_vaga`.
- **Inserção dos Dados**: Os dados são inseridos na tabela `vagas` linha por linha a partir do DataFrame Pandas, usando uma instrução SQL de inserção.
- **Contagem de Registros**: Após a inserção, o número total de registros na tabela é contado e exibido para confirmação.

### 2. **vagas.csv**

Este arquivo contém o dataset de vagas de emprego que será inserido no banco de dados. O arquivo possui as seguintes colunas:

- **Título**: O título da vaga de emprego.
- **Empresa**: O nome da empresa que está ofertando a vaga.
- **Localização**: A localização da vaga (cidade/estado).
- **Data de Publicação**: A data em que a vaga foi publicada ou atualizada.
- **Faixa Salarial**: A faixa salarial oferecida pela vaga (quando disponível).
- **URL da Vaga**: O link para a página original da vaga.

### 3. **vagas.db**

Este é o banco de dados SQLite gerado automaticamente pelo script. Ele contém uma tabela chamada `vagas`, onde as informações extraídas do CSV são armazenadas. A tabela possui os seguintes campos:

- `id_vaga`: Identificador único (chave primária) gerado automaticamente.
- `titulo`: Título da vaga de emprego (obrigatório).
- `empresa`: Nome da empresa (obrigatório).
- `localizacao`: Localização da vaga (obrigatório).
- `data_publicacao`: Data de publicação da vaga (obrigatório).
- `faixa_salarial`: Faixa salarial oferecida (opcional).
- `url_vaga`: URL para a página da vaga (opcional).

## Requisitos do Sistema

Para rodar o projeto, é necessário ter os seguintes componentes instalados:

- Python 3.x
- Bibliotecas:
  - `pandas`
  - `sqlite3` (nativo do Python)

Você pode instalar o Pandas via pip, caso ainda não tenha:

```bash
pip install pandas
