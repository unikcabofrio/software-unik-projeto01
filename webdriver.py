import time, os, random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def InitDriver(hide = False):
    dv_Options = Options()

    agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		]

    agente = agentes[random.randint(0, len(agentes) - 1)]
    dv_Options.add_argument("user-agent=" + agente)
    
    dv_Options.add_argument("--user-data-dir=D:\\Programação\\software-unik-projeto01\\chrome")
    dv_Options.add_argument('--profile-directory=Default')

    if hide == True:
        dv_Options.add_argument('--headless')
        dv_Options.add_argument('--no sandbox')
        dv_Options.add_argument('--mute audio')

    driver = webdriver.Chrome(options=dv_Options)
    driver.set_window_position(0,0)
    driver.set_window_size(800, 750)
    time.sleep(10)
    os.system('cls')
    print(f'[ START ] -> Inicializando Programa')
    return driver

def UrlDriver(driver,url):  
    driver.get(url)
    print(f'[ URL ] -> Carregando Site: {driver.title}') 
    time.sleep(5)

def QuitDriver(driver):
    print(f'\n[ STOP ] -> Finalizando...')   
    driver.quit()

def FindElementXpath(driver,XPath):
    time.sleep(2)
    result = driver.find_element(By.XPATH,XPath)
    return result

def FindElementId(driver,id):
    time.sleep(2)
    result = driver.find_element(By.ID,id)
    return result

def FindElementClassName(driver,className):
    time.sleep(2)
    result = driver.find_element(By.CLASS_NAME,className)
    return result

        