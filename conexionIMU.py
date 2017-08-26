#import time
import serial
#import time
counter=0;
try:
	ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	while (counter<2):
#		time.sleep(1)
		counter+=1;
		if (ser.isOpen()):
			print(" <span class='label-success label label-default'> conectado</span>\n")
			break
		imput=ser.read(81);
		ser.reset_input_buffer();
		#print(imput.decode("utf-8"))
		if(imput):
			print(" <span class='label-success label label-default'> conectado</span>\n")
			break
	else:
		print("</strong> <span class='label-default label label-danger'>Error mensaje</span>\n");
except:
	print("</strong> <span class='label-default label label-danger'>Error Conexion </span>\n")
