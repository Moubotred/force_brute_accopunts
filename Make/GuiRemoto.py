import os
import subprocess

try:

    import ConfigStrem as St
    from PIL import Image, ImageTk
    import playwright

except Exception as e:
    print('[-] librerias no instaladas')
    result = subprocess.run(['pip','install','pillow','selenium','playwright'], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

# https://ftp.mozilla.org/pub/firefox/releases/124.0.2/win64/es-ES/Firefox%20Setup%20124.0.2.exe

import os
import time
import socket
import threading
import tkinter as tk
from io import BytesIO
from tkinter import ttk
import ConfigStrem as St
from tkinter import filedialog
from PIL import Image, ImageTk
from urllib.request import urlopen

def start():
    pass

def salir():
    root.destroy()
    pass

def BuscarTxt():
    namefile = filedialog.askopenfilenames()
    name = namefile[0].split('/')[-1]
    archivo.config(values = "".join(name))    
    archivo.current(0) 

    global directory_file
    directory_file = namefile

def BuscarIp():
    try:
        # Obtener el nombre del host local
        nombre_host = socket.gethostname()
        # Obtener la dirección IP asociada con el nombre del host
        direccion_ip = socket.gethostbyname(nombre_host)
        return direccion_ip,'192.168.0.103'
    except socket.error as e:
        print(f"Error al obtener la dirección IP: {e}")
        return None

def ConexionLocal():

    HOST = '192.168.1.10'
    PORT = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            msg = input("Ingrese plataforma: ")
            data = s.recv(1024)
            msg = data.decode()

            # start_log_thread(msg)

            if msg == "chao":
               break

            s.sendall(bytes(msg, 'utf-8'))
        
    print('Recibido', repr(data))

def Reflejo(msg):
    try:
        RegistroText.insert(tk.END, msg + '\n')
        RegistroText.see(tk.END)  # Desplaza hacia abajo para mostrar la última entrada
        time.sleep(2)
        RegistroText.update()
    except TypeError:
        pass

def Streming(file,streming):
    try:
        is_running = True

        CadenaUsuarios = St.GenCorreo(file,True)

        while is_running:
            Co, Cs = next(CadenaUsuarios)

            if streming == 'Hbo':
                msg = St.Hbo(Co, Cs)
                Reflejo(msg)
            
            if streming == 'Disney':
                msg = St.Disney(Co, Cs)
                Reflejo(msg)

            if streming == 'Crunchyroll':
                msg = St.Crunchyroll(Co, Cs)
                Reflejo(msg)
            
            if streming == 'Netflix':
                msg = St.Netflix(Co, Cs)
                Reflejo(msg)

            if streming == 'Prime Video':
                msg = St.prime(Co, Cs)
                Reflejo(msg)

            # if streming == 'NKookies':
            #     msg = St.Main(Co,Cs)

    except StopIteration:
        print('[+] Finalizo la busqueda de credenciales')
        # Establecer la bandera como falsa para indicar que el hilo ha terminado

def HabilitarRegistro():
    RegistroText.config(state=tk.NORMAL)

def start_log_thread():
    def wrapper():
        try:
            Streming(directory_file[0], plataforma.get())
        except playwright._impl._errors.Error as e:
            if "Executable doesn't exist" in str(e):
                print("Ejecutando instalación de Playwright...")
                subprocess.run(["playwright", "install"])
                print("Instalación de Playwright completada. Reintentando inicio de sesión...")
                Streming(directory_file[0], plataforma.get())

    is_running = False
    if not is_running:
        log_thread = threading.Thread(target=Streming(directory_file[0],plataforma.get()))
        log_thread.start()

def run():
    log_thread = threading.Thread(target=start_log_thread)
    log_thread.start()

root = tk.Tk()
root.title("PANEL DE CONTROL") 
root.geometry("415x500")
root.resizable(False, False)
root.configure(bg="lightblue")

URL = "https://raw.githubusercontent.com/Moubotred/force_brute_accounts/main/Make/imagen.png"
u = urlopen(URL)
raw_data = u.read()
u.close()

img = ImageTk.PhotoImage(data=raw_data) 
label_img = tk.Label(image=img)
label_img.place(x=20, y=20)

Buscarfile = tk.Button(root,text='🔎',command=BuscarTxt)
Buscarfile.place(x=380, y=110)

archivo = ttk.Combobox(root,height=100,width = 24,justify='center',state='disabled')
archivo["values"] = tuple('_')

Btnsalir = tk.Button(root,text='salir',width=6,command = salir)
Btnsalir.place(x=300, y=160)

try:
    archivo.current(0) 
    archivo.place(x=205, y=110) 

except Exception:
    MSG = '''No Hay Archivos TXT en el diretorio
    Cuando hay archivos aparesera la
    configuracion cerra la app iniciar 
    de nuevo '''
    Advertencia = tk.Label(text=MSG)
    Advertencia.place(x=205, y=130)
    
plataforma = ttk.Combobox(root,height=100,width = 30,justify='center')
plataforma["values"] = ("Hbo","NKookies","Crunchyroll", "Disney",'Netflix','Prime Video') 
plataforma.current(0) 
plataforma.place(x=200, y=30)

ips = BuscarIp()
bots = ttk.Combobox(root,height=100,width = 30,justify='center' )
bots["values"] = ips
bots.current(0) 
bots.place(x=202, y=70)

BtnRegistro = tk.Button(root, text="iniciar", width=6, command=run)
BtnRegistro.place(x=240, y=160)

RegistroText = tk.Text(root,height=15, width=45)
RegistroText.place(x=25, y=230)

root.mainloop()