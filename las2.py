import liblas
import sys
import struct
import numpy as np

def main():
	#coeficientes de la matriz de rotacion
	a = b = c = d = e = f = g = h = i = 0.0;
	matrix_rot = np.matrix( ((1,0,0),(0,1,0),(0,0,1)) )
	gravity = np.matrix( ((0,0,0),(0,0,0),(9.8,0,0)) )

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

	data = ""
	rotat = ""
	accel = ""

	data_lidar = ""
	output_lidar = ""
	data_lidar = ""
	data_imu = ""
	data_gps = ""
# for gps
	lat = -33.035385
	lon = -71.595649
	height = 50.0
	phi = lat*3.141592/180
	lamda = lon*3.141592/180

	semi_axis_major = 6378137.0 #metros
	semi_axis_minor = 6356752.314
	eccentricity = 0.08181919
	Radio = semi_axis_major

	x_gps = 1690023.993
	y_gps = -5079111.743
	z_gps = 50.0

	flag_gps = False

	x_min = float('inf')
	x_max = float('-inf')
	y_min = float('inf')
	y_max = float('-inf')
	z_min = float('inf')
	z_max = float('-inf')


	try:
		logs_file = open('output.txt','r')
		las_header = liblas.header.Header()
		las_file = liblas.file.File('./LASFILES/output.las',header=las_header, mode='w');
		for linea in logs_file:
			elementos = linea.strip().split(',')
			#print "holi 1"
			if(len(elementos) == 3):
				#print "holi 2"
				data_lidar = elementos[0]
				data_imu = elementos[1]
				data_gps = elementos[2]
				#print elementos
				#print data_lidar
				#print data_imu
				#print data_gps
			if(data_gps != ""):
				#print "holi 3"
				lat = float(data_imu.strip().split(' ')[3])
				lon = float(data_imu.strip().split(' ')[5])
				height = float(data_imu.strip().split(' ')[8])
				phi = lat*3.141592/180.0
				lamda = lon*3.141592/180.0
				Radio = semi_axis_major/np.sqrt((1 - eccentricity*eccentricity*np.sin(phi)*np.sin(phi)))
				#x_gps = (Radio + height)*np.cos(phi)*np.cos(lamda)
				#y_gps = (Radio + height)*np.cos(phi)*np.sin(lamda)
				#z_gps = height
				flag_gps = True

			if(len(data_imu) == 162):
				#print "holi 4"
				if(data_imu[0:4] == "faff"):
					#print "holi 5"
					rotat = data_imu[14:86]
					accel = data_imu[-70:-46] # se parsea la aceleracion
				if(len(rotat) == 72):
					#print "holi 6"
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
				if(len(accel)==24):
					#print "holi 7"
					a_x_imu = struct.unpack('!f', accel[0:8].decode('hex'))[0]
					a_y_imu = struct.unpack('!f', accel[8:16].decode('hex'))[0]
					a_z_imu = struct.unpack('!f', accel[16:24].decode('hex'))[0]
				#print "holi 8"
				a_x = a_x_imu
				a_y = a_y_imu
				a_z = a_z_imu
				#print "holi 8.3"
				#print matrix_rot
				a_real = matrix_rot.getI()
				#print "holi 8.4"
				a_real = a_real*np.matrix( ((a_x,0,0),(a_y,0,0),(a_z,0,0)) )
				#print "holi 8.5"
				a_x = a_real[0,0]
				a_y = a_real[1,0]
				a_z = a_real[2,0] - gravity[2,0]
				alpha = 0.05
				beta = 0.250
				#print "holi 9"
				if(abs(a_x) < 0.2):
					offset_a_x = a_x*alpha + a_prev_x*(1-alpha)
	#				dev_a_x = (1-beta)*dev_a_x + beta*(abs(a_x - offset_a_x))
				if(abs(a_y) < 0.2):
					offset_a_y = a_y*alpha + a_prev_y*(1-alpha)
	#				dev_a_y = (1-beta)*dev_a_y + beta*(abs(a_y - offset_a_y))
				if(abs(a_z) < 0.2):
					offset_a_z = a_z*alpha + a_prev_z*(1-alpha)
	#				dev_a_z = (1-beta)*dev_a_z + beta*(abs(a_z - offset_a_z))
				a_x -= offset_a_x
				a_y -= offset_a_y
				a_z -= offset_a_z

				a_x = round(a_x,2)
				a_y = round(a_y,2)
				a_z = round(a_z,2)

				j_next_x = (a_x - a_prev_x)/dt
				j_next_y = (a_y - a_prev_y)/dt
				j_next_z = (a_z - a_prev_z)/dt
	#			print "jerk : ", j_x, j_y, j_z
				v_next_x = v_x + round(a_x*dt,6) + round(j_x*dt*dt*0.5,6)
				v_next_y = v_y + round(a_y*dt,6) + round(j_y*dt*dt*0.5,6)
				v_next_z = v_z + round(a_z*dt,6) + round(j_z*dt*dt*0.5,6)
	#			print "velocity :\t", v_next_x, "\t", v_next_y, "\t", v_next_z
				x_next = x + round(v_x*dt,4) + round(a_x*dt*dt*0.5,4) + round(j_x*dt*dt*dt/6.0,4)
				y_next = y + round(v_y*dt,4) + round(a_y*dt*dt*0.5,4) + round(j_y*dt*dt*dt/6.0,4)
				z_next = z + round(v_z*dt,4) + round(a_z*dt*dt*0.5,4) + round(j_z*dt*dt*dt/6.0,4)
	#			print "position :\t", x_next, "\t", y_next, "\t", z_next
	#		asignacion del nuevo estado
				a_prev_x = a_x
				a_prev_y = a_y
				a_prev_z = a_z
				j_x = j_next_x
				j_y = j_next_y
				j_z = j_next_z
	#			if(count%250 == 0):
	#				v_x = 0
	#				v_y = 0
	#				v_z = 0
	#			else:
				v_x = round(v_next_x,6)
				v_y = round(v_next_y,6)
				v_z = round(v_next_z,6)
				x = round(x_next,6)
				y = round(y_next,6)
				z = round(z_next,6)

				if(flag_gps):
					x = y = z = 0.0
	#			print "real position : ", x, y, z
	#			print "tiempo", time.time()
				#count += 1
				#print "holi 10"

			if(len(data_lidar) == 14):
				data_angle = data_lidar[4] + data_lidar[5] + data_lidar[2] + data_lidar[3]
				#print "len :\t", len(data_angle), data_angle
				angle = int(data_angle,16)/16.0
				distance = int((data_lidar[8] + data_lidar[9] + data_lidar[6] + data_lidar[7]),16)
				signal_strength = int((data_lidar[10] + data_lidar[11]),16)
				
				#print "angle :\t",angle, "distancia :\t", distance
				if( ((angle >= 0 and angle <= 360) or (angle >= 337.5 and angle <= 360)) and distance <= 4000 ):
					#print "angle :\t",angle,"cos :\t", np.sin(angle*3.141592/180.0), "distancia :\t", distance
					x_lidar = distance*np.sin(angle*3.141592/180)/100
					z_lidar = -distance*np.cos(angle*3.141592/180)/100
					y_lidar = 0.0
					#print "puntos lidar:\t", x_lidar, "\t", y_lidar, "\t", z_lidar
					vector_lidar_real = matrix_rot*np.matrix( ((x_lidar,0,0),(y_lidar,0,0),(z_lidar,0,0)) )
					
					print "orientacion:\n", matrix_rot*np.matrix(((0,0,0),(0,0,0),(1,0,0)))

					#Xlas = x_gps + x + vector_lidar_real[0,0]
					#Ylas = y_gps + y + vector_lidar_real[1,0]
					#Zlas = z_gps + z + vector_lidar_real[2,0]
					
					Xlas = (lon + (x + vector_lidar_real[0,0])*180/(Radio*3.141592))*3600
					Ylas = (lat + (y + vector_lidar_real[1,0])*180/(Radio*3.141592))*3600
					Zlas = height + z + vector_lidar_real[2,0]


					if(Xlas > x_max):
						x_max = Xlas
					if(Xlas < x_min):
						x_min = Xlas
					if(Ylas > y_max):
						y_max = Ylas
					if(Ylas < y_min):
						y_min = Ylas
					if(Zlas > z_max):
						z_max = Zlas
					if(Zlas < z_min):
						z_min = Zlas
					
					#print "puntos:\t", Xlas, "\t", Ylas, "\t", Zlas

					punto = liblas.point.Point()
					punto.x = Xlas
					punto.y = Ylas
					punto.z = Zlas
		
					las_file.write(punto)
					flag_gps = False
		las_header.min = [x_min,y_min,z_min]
		las_header.max = [x_max,y_max,z_max]
		las_file.close()
		f = open("./LASFILES/listo.las","w")
		f.close()
	except ZeroDivision():
		print "algo salio mal con"
		exit(-1)

if __name__ == '__main__':
	main()

