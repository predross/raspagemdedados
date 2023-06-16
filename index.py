import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Configurando o ChromeDriver usando o ChromeDriverManager
driver_path = ChromeDriverManager().install()
service = Service(driver_path)

# Configurando as opções do navegador
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1200x600")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Inicializando o navegador
driver = webdriver.Chrome(service=service, options=options)

url = "https://divulgacandcontas.tse.jus.br/divulga/#/estados/2020/2030402020/PR/municipios"

driver.get(url)
sleep(3)

# Localizando todos os municípios
todos_municipios = driver.find_elements(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div > section:nth-child(3) > div > div > table > tbody > tr:nth-child(2)")

municipios_data = []

for municipio in todos_municipios:
    # Clicando no município para obter as informações das pessoas
    municipio.click()
    sleep(3)

    todas_pessoas = driver.find_elements(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div > section:nth-child(3) > div > div > table.table.table-hover.visible-md.visible-lg > tbody > tr:nth-child(1) > td:nth-child(1) > a")

    for pessoa in todas_pessoas:
        # Obtendo as informações da pessoa
        pessoa_link = pessoa.get_attribute("href")
        municipios_data.append(pessoa_link)

        driver.get(pessoa_link) # type: ignore
        sleep(3)

        # Pegar as informações pessoais
        nome_pessoas = driver.find_elements(By.CSS_SELECTOR, "body > div.conteudo > div.container-fluid.dvg-main-wrap > div > div:nth-child(1) > section:nth-child(3) > div > div.col-md-7 > div.row > div:nth-child(1) > div > div.text > h3")
         
        nome = driver.find() # type: ignore


        driver.back()
        sleep(2)

    driver.back()
    sleep(2)

driver.quit()

df = pd.DataFrame(municipios_data, columns=["Informacoes"])
print(df)

