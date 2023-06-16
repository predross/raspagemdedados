import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Configurando o navegador
options = webdriver.ChromeOptions()
options.add_argument("--window-size=1200x600")

# Configurando o ChromeDriver usando o ChromeDriverManager
driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)

url = "COLOQUE AQUI SUA URL"

driver.get(url)
sleep(3)


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
        
        for link in pessoa_link:
            
            driver.get(pessoa_link)
            sleep(3)
            
            # Pegar as informação pessoais
            
            
            ###############################
            driver.back()
        
        pessoa_data = pessoa.text
        municipios_data.append(pessoa_data)
    

    driver.back()
    sleep(2)


driver.quit()


df = pd.DataFrame(municipios_data, columns=["Informacoes"])
print(df)
