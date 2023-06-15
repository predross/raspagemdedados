from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

url = "https://divulgacandcontas.tse.jus.br/divulga/#/estados/2020/2030402020/PR/municipios"

# Configurando o navegador
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
options.add_argument('--window-size=1200,600')

# Web driver, que instala o navegador padrão utilizado na máquina do cliente
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def Exec_scrapping():
        
    # Abrir o navegador
    driver.get(url)
    print('- Iniciou o Chrome')
    sleep(6)
    
    def first_scrapping():
        
        #href="#/candidato/2020/2030402020/76910/160001051906"
        # Clicar na imagem para ir na página da notícia
        titulo = driver.find_element(By.CLASS_NAME, 'img-thumbnail')
        print('Print do elemento', titulo)
        titulo.click()
        print('-- click in title')
        sleep(3)
    
    first_scrapping()
    
    def full_scrapping():
           
        # Obter os elementos da página com BeautifulSoup
        page_source = BeautifulSoup(driver.page_source, features="lxml")
        
        print('---------------------------------------------')
        
        titulo = page_source.find('h1', class_='ng-binding')
        # fort_tirulo = titulo.text
        # print(' --TITULO : ',fort_tirulo)
        
        sub_titulo = page_source.find('h2', class_='text-center')
        # format_sub = sub_titulo.text
        # print(' --SUB TITULO : ',format_sub)
        
        get_text = page_source.find('h4', class_='ng-binding')
        # format_text = get_text.text
        # print(' --ARTIGO : ',format_text)
        
        print('---------------------------------------------')

        sleep(7200)
    full_scrapping()
        
while True:
    Exec_scrapping()
