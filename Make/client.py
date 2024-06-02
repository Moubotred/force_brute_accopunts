import socket

def ConexionLocal():

    HOST = '192.168.1.10'
    PORT = 65432        

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        while True:
            msg = input("Ingrese plataforma: ")
            data = s.recv(1024)
            msg = data.decode()

            if msg == "":
               break

            s.sendall(bytes(msg, 'utf-8'))
        
    print('Recibido', repr(data))

