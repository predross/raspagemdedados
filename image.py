import requests
from bs4 import BeautifulSoup
import os

def download_imagens(url, pasta_destino):
    # Fazer a requisição HTTP para obter o conteúdo da página
    response = requests.get(url)
    if response.status_code == 200:
        # Criar uma instância do BeautifulSoup para analisar o HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Encontrar todas as tags de imagem <img> na página
        imagens = soup.find_all('img')
        
        # Criar a pasta de destino se ela não existir
        if not os.path.exists(pasta_destino):
            os.makedirs(pasta_destino)
        
        # Fazer o download de cada imagem encontrada
        for imagem in imagens:
            # Obter o link da imagem
            link_imagem = imagem['src']
            
            # Fazer o download da imagem
            response_imagem = requests.get(link_imagem)
            
            # Obter o nome do arquivo a partir do link da imagem
            nome_arquivo = os.path.join(pasta_destino, os.path.basename(link_imagem))
            
            # Salvar a imagem no disco
            with open(nome_arquivo, 'wb') as arquivo:
                arquivo.write(response_imagem.content)
                print(f"Imagem salva: {nome_arquivo}")
    else:
        print("Erro ao obter a página.")

# Exemplo de uso
url_pagina = 'hhttps://divulgacandcontas.tse.jus.br/divulga/#/estados/2020/2030402020/PR/municipios'
pasta_destino = 'Documentos'

download_imagens(url_pagina, pasta_destino)
