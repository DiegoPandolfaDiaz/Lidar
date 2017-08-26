import serial
import time
import sys
import struct
import numpy as np

try:
	ser_imu = serial.Serial(
		port='/dev/ttyUSB0',
		baudrate=115200,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)

	ser_lidar = serial.Serial(
		port='/dev/ttyUSB1',
		baudrate=115200,
		parity=serial.PARITY_NONE,
		stopbits=serial.STOPBITS_ONE,
		bytesize=serial.EIGHTBITS
	)

	

except:
	print "dispositivo no conectado, intente de nuevo por favor"
	exit()

##### variables auxiliares
ax = 0.0
ay = 0.0
az = 0.0

#obteniendo gravedad
ser_imu.flush()
count = 0
data = ""
g_x = 0
g_y = 0
g_z = 0
accel_g = ""
print "calibrando ..."
while(count < 2000):
	if(ser_imu.inWaiting()>0):
		data = ser_imu.read(81)
		ser_imu.flushInput()
		count += 1
	if(data.encode("hex")[0:4] == "faff"):
		accel_g = data.encode("hex")[-70:-46] # se parsea la aceleracion
	if(len(accel_g)==24):
		g_x = struct.unpack('!f', accel_g[0:8].decode('hex'))[0]*0.001 + g_x*0.999 # se promedia
		g_y = struct.unpack('!f', accel_g[8:16].decode('hex'))[0]*0.001 + g_y*0.999
		g_z = struct.unpack('!f', accel_g[16:24].decode('hex'))[0]*0.001 + g_z*0.999

# se inicializa la gravedad y la matriz de rotacion
gravity = np.matrix( ((0,0,0),(0,0,0),(np.sqrt(g_x*g_x + g_y*g_y + g_z*g_z),0,0)) )#np.matrix( ((0,0,0),(0,0,0),(9.80665,0,0)) )
print "ready ..."
time.sleep(0.5)
print "gravedad : ", gravity
time.sleep(2)
matrix_rot = np.matrix( ((1,0,0),(0,1,0),(0,0,1)) )

#posiciones
x_next = 0.0
y_next = 0.0
z_next = 0.0
x = 0.0
y = 0.0
z = 0.0

#velocidades
v_next_x = 0.0
v_next_y = 0.0
v_next_z = 0.0
v_x = 0.0
v_y = 0.0
v_z = 0.0

#aceleraciones
a_prev_x = 0.0
a_prev_y = 0.0
a_prev_z = 0.0
a_x_imu = 0.0 #esta sera la medicion de la imu
a_y_imu = 0.0
a_z_imu = 0.0
a_x = 0.0
a_y = 0.0
a_z = 0.0

#jerk
j_next_x = 0.0
j_next_y = 0.0
j_next_z = 0.0
j_x = 0.0
j_y = 0.0
j_z = 0.0

#difencial de tiempo
dt = 0.001 #de alguna manera hay que medir el tiempo entre samples del lidar

#intervalo confiable y correccion de offset
alpha = 0.0
offset_a_x = 0.0
offset_a_y = 0.0
offset_a_z = 0.0
beta = 0.0
dev_a_x = 0.0
dev_a_y = 0.0
dev_a_z = 0.0

ser_imu.flush()
data = ""
rotat = ""
accel = ""

count = 0
while(True):
	if(ser_imu.inWaiting()>0):
		data = ser_imu.read(81)
		ser_imu.flushInput()
#		print data.encode("hex")
	if(data.encode("hex")[0:4] == "faff"):
		rotat = data.encode("hex")[14:86] #se parsea matriz de rotacion
#	print rotat
	if(len(rotat) == 72):
		a = struct.unpack('!f', rotat[0:8].decode('hex'))[0]
		b = struct.unpack('!f', rotat[8:16].decode('hex'))[0]
		c = struct.unpack('!f', rotat[16:24].decode('hex'))[0]
		d = struct.unpack('!f', rotat[24:32].decode('hex'))[0]
		e = struct.unpack('!f', rotat[32:40].decode('hex'))[0]
		f = struct.unpack('!f', rotat[40:48].decode('hex'))[0]
		g = struct.unpack('!f', rotat[48:56].decode('hex'))[0]
		h = struct.unpack('!f', rotat[56:64].decode('hex'))[0]
		i = struct.unpack('!f', rotat[64:72].decode('hex'))[0]
		matrix_rot = np.matrix( ((a,b,c),(d,e,f),(g,h,i)) )
#		print matrix_rot
#	gravity_rot = matrix_rot * gravity # gravedad en el espacio de la imu
#	v_gravity_rot = np.array([gravity_rot[0,0], gravity_rot[1,0], gravity_rot[2,0]])
#	print "vector rotado : ", v_gravity_rot
	if(data.encode("hex")[0:4] == "faff"):
		accel = data.encode("hex")[-70:-46] # se parsea la aceleracion
	if(len(accel)==24):
		a_x_imu = struct.unpack('!f', accel[0:8].decode('hex'))[0] #- np.dot(np.array([1,0,0]),v_gravity_rot)
		a_y_imu = struct.unpack('!f', accel[8:16].decode('hex'))[0] #- np.dot(np.array([0,1,0]),v_gravity_rot)
		a_z_imu = struct.unpack('!f', accel[16:24].decode('hex'))[0] #- np.dot(np.array([0,0,1]),v_gravity_rot)

# aceleraciones en el espacio generado por los ejes de la imu
	a_x = a_x_imu #round(a_x_imu, 6)
	a_y = a_y_imu #round(a_y_imu, 6)
	a_z = a_z_imu #round(a_z_imu, 6)

# aceleraciones en el plano real (menos la gravedad)
	a_real = matrix_rot.getI()*np.matrix( ((a_x,0,0),(a_y,0,0),(a_z,0,0)) )
	a_x = a_real[0,0]
	a_y = a_real[1,0]
	a_z = a_real[2,0] - gravity[2,0]
#	print "acceleraion :\t", a_x, "\t", a_y, "\t", a_z

# correcciones de offset y varianza para intervalo confiable
	alpha = 0.05
	beta = 0.250
	if(abs(a_x) < 0.2):
		offset_a_x = a_x*alpha + a_prev_x*(1-alpha)
#		dev_a_x = (1-beta)*dev_a_x + beta*(abs(a_x - offset_a_x))
	if(abs(a_y) < 0.2):
		offset_a_y = a_y*alpha + a_prev_y*(1-alpha)
#		dev_a_y = (1-beta)*dev_a_y + beta*(abs(a_y - offset_a_y))
	if(abs(a_z) < 0.2):
		offset_a_z = a_z*alpha + a_prev_z*(1-alpha)
#		dev_a_z = (1-beta)*dev_a_z + beta*(abs(a_z - offset_a_z))

#	print "1 aceleracion :\t", a_x, "\t", a_y, "\t", a_z
	a_x -= offset_a_x
	a_y -= offset_a_y
	a_z -= offset_a_z

	a_x = round(a_x,4)
	a_y = round(a_y,4)
	a_z = round(a_z,4)
##	if(abs(a_x - offset_a_x) < 2*dev_a_x ):
##		a_x = 0.0
##	else:
##		pass
##	if(abs(a_y - offset_a_y) < 2*dev_a_y ):
##		a_y = 0.0
##	else:
##		pass
##	if(abs(a_z - offset_a_z) < 2*dev_a_z ):
##		a_z = 0.0
##	else:
##		pass

#	print "2 offset :\t", offset_a_x, "\t", offset_a_y, "\t", offset_a_z
#	print "3 aceleracion_off :\t", a_x, "\t", a_y, "\t", a_z
#	print "dev :\t", dev_a_x, "\t", dev_a_y, "\t", dev_a_z


#calculo del nuevo estado
	j_next_x = (a_x - a_prev_x)/dt
	j_next_y = (a_y - a_prev_y)/dt
	j_next_z = (a_z - a_prev_z)/dt
#	print "jerk : ", j_x, j_y, j_z
	v_next_x = v_x + round(a_x*dt,6) + round(j_x*dt*dt*0.5,6)
	v_next_y = v_y + round(a_y*dt,6) + round(j_y*dt*dt*0.5,6)
	v_next_z = v_z + round(a_z*dt,6) + round(j_z*dt*dt*0.5,6)
#	print "velocity :\t", v_next_x, "\t", v_next_y, "\t", v_next_z
	x_next = x + round(v_x*dt,4) + round(a_x*dt*dt*0.5,4) + round(j_x*dt*dt*dt/6.0,4)
	y_next = y + round(v_y*dt,4) + round(a_y*dt*dt*0.5,4) + round(j_y*dt*dt*dt/6.0,4)
	z_next = z + round(v_z*dt,4) + round(a_z*dt*dt*0.5,4) + round(j_z*dt*dt*dt/6.0,4)
#	print "position :\t", x_next, "\t", y_next, "\t", z_next
#asignacion del nuevo estado
	a_prev_x = a_x
	a_prev_y = a_y
	a_prev_z = a_z
	j_x = j_next_x
	j_y = j_next_y
	j_z = j_next_z
#	if(count%250 == 0):
#		v_x = 0
#		v_y = 0
#		v_z = 0
#	else:
	v_x = round(v_next_x,6)
	v_y = round(v_next_y,6)
	v_z = round(v_next_z,6)
	x = round(x_next,6)
	y = round(y_next,6)
	z = round(z_next,6)
	print "real position : ", x, y, z
#	print "tiempo", time.time()
	count += 1

