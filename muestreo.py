
import time
import sys
import serial
def main():

	try:
		ser_imu = serial.Serial(
			port='/dev/ttyUSB1',
			baudrate=115200,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)

		ser_lidar = serial.Serial(
			port='/dev/ttyUSB0',
			baudrate=115200,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)
		ser_gps = serial.Serial(
			port='/dev/ttyACM0',
			baudrate=115200,
			parity=serial.PARITY_NONE,
			stopbits=serial.STOPBITS_ONE,
			bytesize=serial.EIGHTBITS
		)

		file=open("output.txt",'w');
		config_file = open("configuraciones.txt",'r')
	except(serial.serialutil.SerialException()):
		print "conecte los dispositivos, intentelo de nuevo por favor"
		exit(1)

	print "configurando lidar..."
	# se configura el lidar
	ser_lidar.flushOutput()
	ser_lidar.write('DX'+ '\n')
	print "se detiene la adquisicion de datos"
	time.sleep(0.5)
	ser_lidar.flush()
	lines = config_file.readlines()
	ser_lidar.flushInput()
	ser_lidar.flushOutput()
	ser_lidar.write('LR' + lines[0].split(';')[1])
	print "se setean los samples"
	time.sleep(0.5)
	status = ""
	while(ser_lidar.inWaiting()>0):
		status = ser_lidar.read(9)
		ser_lidar.flushInput()
		print "status : ", status
	if(len(status) == 9):
		print "[5:7] : ", status[5:7]
		if(status[5:7] == "00"):
			pass
		else:
			exit(-1)
	line = lines[1]
	ser_lidar.flushOutput()
	ser_lidar.write('MS' + line.split(';')[1])
	print "se setea la velocidad del motor"
	time.sleep(10)
	status = ""
	while(ser_lidar.inWaiting()>0):
		status = ser_lidar.read(9)
		ser_lidar.flushInput()
		print "status 2: ", status
	if(len(status) == 9):
		print "[5:7] : ", status[5:7]
		if(status[5:7] == "00"):
			pass
		else:
			exit(-1)

	print "ready ..."
	#cmd = raw_input("ingrese comando de lidar : ")
	cmd = "DS" #data start adquisition
	ser_lidar.write(cmd + "\n")
	time.sleep(1)
	ser_lidar.flushInput()
	ser_imu.flushInput()
	ser_gps.flushInput()

	out = ''
	input_serial_gps= ''
	input_serial_lidar = ''
	input_serial_imu = ''
	while(1):
		if(ser_gps.inWaiting()>0):
			input_serial_gps = ser_gps.readline().decode('UTF-8').strip()
			ser_gps.flushInput()

		if(ser_imu.inWaiting()>0):
			input_serial_imu = ser_imu.read(81)
			input_serial_imu = input_serial_imu.encode("hex")
			ser_imu.flushInput()
			#out += "," + input_serial.encode("hex")
			#print out.encode("hex")
			#print ","
			#print input_serial_imu[0:2], input_serial_lidar[0:4]

		if(ser_lidar.inWaiting()>0):
			input_serial_lidar = ser_lidar.read(7)
			input_serial_lidar = input_serial_lidar.encode("hex")
			ser_lidar.flushInput()
			if(input_serial_lidar[0:2] == "00" and input_serial_imu[0:4] == "faff"):
				out = input_serial_lidar + "," + input_serial_imu + "," + input_serial_gps
				file.write(out+'\n');
			#out += "," + input_serial_lidar.encode("hex") + "," + input_serial_imu.encode("hex")
		#out = input_serial_lidar.encode("hex") + "," + input_serial_imu.encode("hex")
	#	if(out != ''):
	#		file.write(out+'\n');
	file.close()

if __name__ == '__main__':
	main()
