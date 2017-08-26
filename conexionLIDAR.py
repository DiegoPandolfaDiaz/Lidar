import sys
import serial
import time
counter=0;
try:
	ser = serial.Serial(
    port='/dev/ttyUSB1', 
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS
)
	while (counter<2):
		if (ser.isOpen()):
			print(" <span class='label-success label label-default'> conectado</span>\n")
			break
		ser.write("DS\n");
		time.sleep(1)
		counter+=1;
		imput=ser.read(7);
		ser.reset_input_buffer();
		#print(imput.decode("utf-8"))
		if(imput):
			sys.stdout.write(" <span class='label-success label label-default'> conectado</span>\n")
			break
	else:
		sys.stdout.write("</strong> <span class='label-default label label-danger'>Error2</span>\n");
except:
	sys.stdout.write("</strong> <span class='label-default label label-danger'>Error1 </span>\n")
