from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.firefox import GeckoDriverManager
import random

# Lista de User-Agents que quieres utilizar
user_agents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
    # Agrega más User-Agents según tus necesidades
]

# Crear una instancia del navegador Firefox
options = webdriver.FirefoxOptions()

# Iterar a través de las URLs y User-Agents
for url in ["https://www.ejemplo.com", "https://www.ejemplo.com"]:
    user_agent = random.choice(user_agents)
    
    # Establecer el User-Agent en las opciones del navegador
    options.set_preference("general.useragent.override", user_agent)
    
    # Crear una instancia del navegador con Geckodriver
    driver = webdriver.Firefox(options=options)    
    # Visitar la URL
    driver.get(url)

    print(driver.execute_script("return navigator.userAgent;"))
    
    # Realizar aquí las acciones que necesites en la página
    
    # Cerrar el navegador después de usarlo
    driver.quit()
print(Fore.YELLOW+f'Email:{Fore.WHITE+Email}',Fore.YELLOW+f' Password:{Fore.WHITE+Password}',Fore.YELLOW+f' Status:{Fore.RED+resp}')