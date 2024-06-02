import tkinter as tk
from tkinter import scrolledtext
import threading
import time
import ConfigStrem as St

class LogViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Log Viewer")

        # Widget Text para mostrar el log
        self.log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
        self.log_text.pack(expand=True, fill=tk.BOTH)

        # Botón para agregar una entrada de log de ejemplo
        self.btn_add_log = tk.Button(root, text="Iniciar", command=self.start_log_thread)
        self.btn_add_log.pack()

        # Bandera para controlar la ejecución del hilo
        self.is_running = False

    def start_log_thread(self):
        # Verificar si el hilo ya está en ejecución
        if not self.is_running:
            # Crear un hilo para ejecutar el bucle en segundo plano
            log_thread = threading.Thread(target=self.add_log_entries_thread)
            # Establecer la bandera como verdadera para indicar que el hilo está en ejecución
            self.is_running = True
            # Iniciar el hilo
            log_thread.start()

    def add_log_entries_thread(self):
        try:
            CadenaUsuarios = St.GenCorreo('Cuentas_Strem_1.txt')
            while self.is_running:
                Co, Cs = next(CadenaUsuarios)
                msg = St.Netflix(Co, Cs)

                # log_message = Cs+Co+'\n'
                self.log_text.insert(tk.END, msg + '\n')
                self.log_text.see(tk.END)  # Desplaza hacia abajo para mostrar la última entrada
                time.sleep(2)
                self.log_text.update()
        except StopIteration:
            print('[+] Finalizo el script')
            # Establecer la bandera como falsa para indicar que el hilo ha terminado
            self.is_running = False

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = LogViewerApp(root)
#     root.mainloop()

def add_log_entries_thread():
        try:
            is_running = True
            CadenaUsuarios = St.GenCorreo('Cuentas_Strem_1.txt')
            while is_running:
                Co, Cs = next(CadenaUsuarios)
                msg = St.Netflix(Co, Cs)

                # # log_message = Cs+Co+'\n'
                # log_text.insert(tk.END, msg + '\n')
                # log_text.see(tk.END)  # Desplaza hacia abajo para mostrar la última entrada
                # time.sleep(2)
                # log_text.update()

        except StopIteration:
            print('[+] Finalizo el script')
            # Establecer la bandera como falsa para indicar que el hilo ha terminado
            # is_running = False

def start_log_thread():
    # Verificar si el hilo ya está en ejecución
    is_running = False
    if not is_running:
        # Crear un hilo para ejecutar el bucle en segundo plano
        # is_running = True
        log_thread = threading.Thread(target=add_log_entries_thread)
        # Establecer la bandera como verdadera para indicar que el hilo está en ejecución
        # Iniciar el hilo
        log_thread.start()

# root = root
        
root = tk.Tk()
root.title("Log Viewer")
# get Text para mostrar el log
log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
log_text.pack(expand=True, fill=tk.BOTH)
# ón para agregar una entrada de log de ejemplo
btn_add_log = tk.Button(root, text="Iniciar", command=start_log_thread)
btn_add_log.pack()

root.mainloop()