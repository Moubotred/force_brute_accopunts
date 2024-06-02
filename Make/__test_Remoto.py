import socket

HOST = '192.168.1.104'  # Cambiar por la dirección IP del servidor si es necesario
PORT = 65432  # Mismo puerto que el servidor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    comando = input("Ingrese un comando: ")
    client_socket.send(comando.encode('utf-8'))
    # Esperar respuesta del servidor si es necesario
    # Procesar la respuesta recibida

client_socket.close()
