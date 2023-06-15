import gspread
from google.oauth2 import service_account
import json

# Configuração das credenciais da API do Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = service_account.Credentials.from_service_account_file('credentials.json', scopes=scope)
client = gspread.authorize(credentials)

# Abrir a planilha pelo link de referência
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1laTMUrXzBYD0uVF3vF5HMxXvENgK-TVl0biupcxYU2k/edit#gid=0')

# Selecionar a planilha específica pelo nome
worksheet = spreadsheet.worksheet('Nome da Planilha')

# Função para salvar os dados na planilha
def save_to_sheet(data):
    # Obter a próxima linha vazia para adicionar os dados
    next_row = len(worksheet.get_all_values()) + 1

    # Converter os dados em uma lista de valores
    values = [data['titulo'], data['subtitulo'], data['texto']]

    # Adicionar os valores na próxima linha da planilha
    worksheet.insert_row(values, next_row)

# Ler dados do arquivo JSON
with open('dados.json') as json_file:
    dados = json.load(json_file)

# Chamar a função para salvar os dados na planilha para cada conjunto de dados no JSON
for data in dados:
    save_to_sheet(data)
