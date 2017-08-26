import socket
import sys
servidor = "127.0.0.1"
puerto = 9999

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((servidor, puerto))
#print sys.argv[1]
cliente.send(sys.argv[1]);
#respuesta = cliente.recv(4096)
#print respuesta
