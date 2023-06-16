import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import openpyxl

# Configurando o ChromeDriver usando o ChromeDriverManager
driver_path = ChromeDriverManager().install()
service = Service(driver_path)

# Configurando as opções do navegador
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1200x600")
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Adicionado para suprimir as mensagens de erro

# Inicializando o navegador
driver = webdriver.Chrome(service=service, options=options)

def collect_data(url):
    driver.get(url)
    sleep(3)

    # Localizando todos os municípios
    todos_municipios = driver.find_elements(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div > section:nth-child(3) > div > div > table > tbody > tr > td > a > div")

    municipios_data = []

    for municipio in todos_municipios[:399]:  # Ajuste para percorrer 399 cidades
        # Clicando no município para obter as informações dos candidatos
        municipio.click()
        sleep(3)

        # Localizando os candidatos de cada tipo (prefeito, vice, vereador)
        tipos_candidatos = driver.find_elements(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div > div > table > tbody > tr > td:nth-child(1) > select > option")

        for tipo in tipos_candidatos:
            # Clicando no tipo de candidato para obter as informações
            tipo.click()
            sleep(3)

            # Obtendo as informações do candidato
            nome_completo = driver.find_element(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div:nth-child(1) > section:nth-child(3) > div > div.col-md-7 > div.row > div:nth-child(1) > div > div.text > h3").text
            site = ""
            if driver.find_elements(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div:nth-child(1) > section:nth-child(3) > div > div.col-md-7 > div.row > div:nth-child(11) > div > div.text > h3.social-midia.ng-scope > a"):
                site = driver.find_element(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div:nth-child(1) > section:nth-child(3) > div > div.col-md-7 > div.row > div:nth-child(11) > div > div.text > h3.social-midia.ng-scope > a").get_attribute("href")
            total_recursos_recebidos = driver.find_element(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div:nth-child(2) > section:nth-child(2) > div > div:nth-child(2) > div:nth-child(2) > div > div > h2.ng-binding").text
            total_despesas = driver.find_element(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div:nth-child(2) > section:nth-child(2) > div > div:nth-child(3) > div:nth-child(3) > div > div > h3.ng-binding").text

            # Salvando as informações em uma lista
            municipios_data.append([nome_completo, site, total_recursos_recebidos, total_despesas])

    return municipios_data

base_url = "https://divulgacandcontas.tse.jus.br/divulga/#/estados/2020/2030402020/PR/municipios"
dados_municipios = collect_data(base_url)

# Salvando os dados em um arquivo Excel
arquivo_excel = "dados.xlsx"
df = pd.DataFrame(dados_municipios, columns=["Nome Completo", "Site", "Total Recursos Recebidos", "Total Despesas"])
df.to_excel(arquivo_excel, index=False)

# Fechando o navegador
driver.quit()
