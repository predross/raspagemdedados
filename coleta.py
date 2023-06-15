# Importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
from time import sleep
import re

url = "https://divulgacandcontas.tse.jus.br/divulga/#/estados/2020/2030402020/PR/municipios"

#Configurando o navegador
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument( 'options.add_argument( window-size=1200 x 600 )' )

#web-driver, que instalado o navegador padrão utilizado na maquina do cliente
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), chrome_options=options)

def Exec_scrapping():
        
    #Abrir o navegador
    resposta = driver.get(url)
    resposta
    print('- Iniciou o Chrome')
    sleep(6)
    
    def fist_scrapping():
        
        # click na imagem para ir na página da noticia
        titulo = driver.find_element(By.CLASS_NAME, 'elementor-post__thumbnail')
        print('PRint do element',titulo)
        titulo.click()
        print('-- click in title ')
        sleep(3)
    
    fist_scrapping()
    
    #get url
    
        
    
    def full_scrapping():
           
        # Obter os elementos da página com BeautifulSoup
        page_source = BeautifulSoup(driver.page_source, features="lxml")
        
        print('---------------------------------------------')
        
        titulo = page_source.find('h1', class_ = '')
        fort_tirulo = titulo.text
        print(' --TITULO : ',fort_tirulo)
        
        sub_titulo = page_source.find('h2', class_ = '')
        format_sub = sub_titulo.text
        print(' --SUB TITULO : ',format_sub)
        
        get_text = page_source.find('div', class_ = 'entry-')
        format_text = get_text.text
        print(' --ARTIGO : ',format_text)
        
        print('---------------------------------------------')

        sleep(7200)
    full_scrapping()
        
        
        
while True:
    
    Exec_scrapping() 



    