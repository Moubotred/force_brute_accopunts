import os
import time
import threading
import socket
import tkinter as tk
# import Pt_Brute_v0 as St
import ConfigStrem as St
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import scrolledtext

def BuscarTxt(directorio):
    archivos_txt = []
    for archivo in os.listdir(directorio):
        if archivo.endswith(".txt"):
           archivos_txt.append(archivo)
    return archivos_txt

def Reflejo(msg):
    log_text.insert(tk.END, msg + '\n')
    log_text.see(tk.END)  # Desplaza hacia abajo para mostrar la última entrada
    time.sleep(2)
    log_text.update()

def Streming(file,streming,is_running):
    
    CadenaUsuarios = St.GenCorreo(file,True)
    while is_running:
        try:

            Co, Cs = next(CadenaUsuarios)

            if streming == 'Crunchyroll':
                msg = St.Crunchyroll(Co, Cs)
                Reflejo(msg)

            if streming == 'Disney':
                msg = St.Disney(Co, Cs)
                Reflejo(msg)

            if streming == 'Hbo':
                msg = St.Hbo(Co, Cs)
                Reflejo(msg)
            
            if streming == 'Netflix':
                msg = St.Netflix(Co, Cs)
                Reflejo(msg)

        except StopIteration:
            print('[+] Finalizo el script')
            # Establecer la bandera como falsa para indicar que el hilo ha terminado
            is_running = False

def BuscarIp():
    try:
        # Obtener el nombre del host local
        nombre_host = socket.gethostname()
        # Obtener la dirección IP asociada con el nombre del host
        direccion_ip = socket.gethostbyname(nombre_host)
        return direccion_ip
    except socket.error as e:
        print(f"Error al obtener la dirección IP: {e}")
        return None

def BorrarRegistro(text):
    # Limpiar el área de captura
    text.delete(1.0, tk.END)

def HabilitarRegistro():
    log_text.config(state=tk.NORMAL)

def RegistoSegundoPlano():

    is_running = False

    HabilitarRegistro()
    # Verificar si el hilo ya está en ejecución
    if not is_running:
        # Crear un hilo para ejecutar el bucle en segundo plano
        log_thread = threading.Thread(target=Streming(cuentas.get(),strem.get(),not(is_running)))
        # Establecer la bandera como verdadera para indicar que el hilo está en ejecución
        # is_running = True
        # Iniciar el hilo
        log_thread.start()

root = tk.Tk()
root.title("PANEL DE CONTROL") 
root.geometry("400x500")
root.configure(bg="lightblue")

img = ImageTk.PhotoImage(Image.open("imagen.png"))  
label_img = tk.Label(image=img)
label_img.place(x=20, y=20)

files = BuscarTxt(os.path.join(os.getcwd(),'txt'))
cuentas = ttk.Combobox(root)
cuentas["values"] = tuple(files)

cuentas.current(0) 
cuentas.place(x=200, y=60) 

strem = ttk.Combobox(root)
strem["values"] = ("Hbo", "Crunchyroll", "Disney") 

strem.current(0) 
strem.place(x=200, y=30)

ips = BuscarIp()
bots = ttk.Combobox(root)
bots["values"] = ips
bots.current(0) 
bots.place(x=100, y=200)

boton = tk.Button(root, text="Iniciar", command=RegistoSegundoPlano)
boton.place(x=250, y=120)

log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20,state = tk.DISABLED)
log_text.place(x=25, y=230)

root.mainloop()

