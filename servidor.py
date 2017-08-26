# -*- coding: utf-8 -*-

import socket
import sys
import thread
from string import maketrans
from datetime import  *
import las
import muestreo
import os

__NGrupos=26

global a
def clientthread(conn):
    #Sending message to connected client
    #conn.send('Bienvenido a las Exp 2 redes 2016!'.encode("utf-8")) #send only takes string
    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        #reply = 'Mensaje Recibido!!!'
        data = conn.recv(1024)
	print data
        if data=="1":
            #muestreo.main()
            a=threading.current_thread();
            print(a)
        elif data =="0":
            os.system("pkill -f muestreo.py");
        #conn.sendall("Porfavor ingrese el numero de su grupo!")
        elif data=="2":
            las.main()
            a=threading.current_thread();
            print(a)
        elif data=="3":
            os.system("echo hola > /var/www/html/ola.txt");
        break

    conn.close()

HOST = '127.0.0.1'   # Symbolic name meaning all available interfaces
PORT = 9999
#archivo_fuente=open("fuentes.txt",'r')
#lineas=archivo_fuente.readlines()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created\n'

try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'

s.listen(10)
print 'Socket now listening'

while True:
    #wait to accept a connection
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    #start new thread
    try:
        thread.start_new_thread(clientthread ,(conn,))
    except Exception as e:
        pass
    
s.close()

