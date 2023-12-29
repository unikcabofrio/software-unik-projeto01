import time
from webdriver import *

ddd = ['22']
codArea = ['55']
Sufixo = {
    0:['99600-99653','99700-99999'],
    1:['98100-98187','98800-98839','98841-98849','98851-98854','98857-98859','98861-98879'],
    2:['97400-97406','99101-99105','99200-99219','99221-99229','99231-99239','99241-99249','99251-99259','99261-99269','99271-99279','99281-99293']
}
listContatos = []

def checkNumber(key,name,listContatos,driver):
    # 
    key = int(key)
    count = 0
    lastNumber = 0
    # 
    if len(listContatos) > 0:
        lastNumber = listContatos[-1].strip()
        lastNumber = lastNumber.split('-')
        lastNumber = int(lastNumber[1])+1
    # 
    for sufix in Sufixo[key]:
        splitSufix = sufix.split('-')
        # 
        for i_sufix in range(int(splitSufix[0]),int(splitSufix[1])+1):
            # 
            for i in range(lastNumber,10000):
                sufix_contato = '{:d}'.format(i).zfill(4)
                contato = f'{ddd[0]}{i_sufix}-{sufix_contato}'
                print(f'[ INFO ] -> Verificando Contato: {contato}: ',end=' ')
                # 
                driver.get(f'https://web.whatsapp.com/send/?phone={codArea[0]}{contato}')
                time.sleep(15)
                # 
                try:
                    result = FindElementXpath(driver,'/html/body/div[1]/div/span[2]/div/span/div/div/div/div/div/div[1]').get_attribute('innerText')
                    if result == 'O número de telefone compartilhado por url é inválido.':
                        print('INVALIDO')
                # 
                except:
                    print('VALIDO')
                    count = count + 1
                    listContatos.append(contato)
                # 
                if count == 10:
                    print(f'\n[ INFO ] -> Salvando lista de contatos\n')
                    count = 0
                    with open(f"contato{name}.txt", 'w') as file:
                        for item in listContatos:
                            file.write(str(item)+'\n')
                # 
                time.sleep(1)        

def InitContato(driver):
    global listContatos
    # 
    typeOperadora = input(f'\n[ WARNING ] -> Qual Operadora desejar fazer a verificação? [0 = VIVO | 1 = TIM | 2 = CLARO ] :')
    #
    name = 'Vivo' if typeOperadora == '0' else 'Tim' if typeOperadora == '1' else 'Claro'
    # 
    if os.path.exists(f"contato{name}.txt"):
        with open(f"contato{name}.txt", 'r') as arquivo:
            listContatos = [linha.strip() for linha in arquivo.readlines()]
    # 
    print(f'\n[ INFO ] -> Você selecionou a operadora ( {name} )')
    #    
    print(f'\n[ INFO ] -> Total de contatos Salvos:  ( {len(listContatos)} )')
    print(f'[ INFO ] -> Inicializando Verificação\n')
    #
    checkNumber(typeOperadora,name,listContatos,driver)


# def GeradordeNumeros(key,name):
#     path = f"contato{name}.txt"
#     listContatos = []
#     for sufix in Sufixo[key]:
#         splitSufix = sufix.split('-')
#         for i_sufix in range(int(splitSufix[0]),int(splitSufix[1])+1):
#             for i in range(10000):
#                 contato = f'{ddd[0]}{i_sufix}-'+'{:d}'.format(i).zfill(4)
#                 listContatos.append(contato)

#     with open(path, 'w') as file:
#         for item in listContatos:
#             file.write(str(item)+'\n')

# GeradordeNumeros(0,'Vivo')
# GeradordeNumeros(1,'Tim')
# GeradordeNumeros(2,'Claro')