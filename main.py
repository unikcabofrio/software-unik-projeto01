import os
from webdriver import *
from contato import *
   
try:
    # 
	# Inicializando Driver
    os.system('cls')
    hideInfo = input(f'\n[ WARNING ] -> Deseja Ocultar o Navegador? [0 = Sim | 1 = Não ] :')
    hideInfo = True if hideInfo == '0' else False
    driver = InitDriver(hideInfo)
    # 
    # Carregando site
    UrlDriver(driver,'https://web.whatsapp.com/')
    # 
    # Verificando Se o usuário está conectado
    conected = input(f'\n[ WARNING ] -> O Whatsapp Foi Conectado? [0 = Sim | 1 = Não ] :')
    # 
    if conected in '0':
        InitContato(driver)
    # 
    # Fechando Driver
    QuitDriver(driver)
# 
except KeyboardInterrupt:
    print(f'\n[ STOP ] -> Programa Finalizado pelo ( USUÁRIO )')   
# 
except Exception as Err:
    print(f'\n[ ERRO ] -> {Err}')
      


