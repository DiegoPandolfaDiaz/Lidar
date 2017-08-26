import sys
import serial
import time
import signal
counter=0;
def signal_handler(signum, frame):
    raise Exception("Timed out!")
#signal.signal(signal.SIGALRM, signal_handler)
#signal.alarm(5)

try:
	try:
		ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS)
	except Exception, msg:
    		pass
	while (True):
		time.sleep(1)
		counter+=1;
		if (ser.isOpen()):
			print(" <span class='label-success label label-default'> conectado</span>\n")
			#break
		imput=ser.read(7);
		ser.reset_input_buffer();
		#print(imput.decode("utf-8"))
		if(imput):
			print imput
			#sys.stdout.write(" <span class='label-success label label-default'> conectado</span>\n")
			#break
	else:
		sys.stdout.write("</strong> <span class='label-default label label-danger'>Error lectura</span>\n");
except NameError:
	sys.stdout.write("</strong> <span class='label-default label label-danger'>Error conexion </span>\n")
