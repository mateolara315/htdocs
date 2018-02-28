from datetime import datetime, date, time, timedelta
import calendar

import socket
import pymysql.cursors
import struct
import textwrap


def main():

	mateo = pymysql.connect(user='root', password='12345',
							host='127.0.0.1',
							database='fredym')

	cursor = mateo.cursor()

	insertar = ("INSERT INTO syrus"
				"(hora, latitud, longitud) "
				"VALUES (%s, %s, %s)")

	conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	conn.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	HOST = "192.168.0.6"
	conn.bind((HOST, 47857))

	while True:
		raw_data,addr = conn.recvfrom(65536)
		data = raw_data.decode("utf-8")
		if data[0:4] == ">REV":
			print("EL DATO QUE LLEGO "+data)
			lat = (data[16:19]+"."+data[19:24])
			lon = (data[24:28] + "." + data[28:33])
			fecha = int(float(data[6:10]))
			fecha = date(1980, 1, 6) + timedelta(weeks=fecha) #ojo es 6 ver problema Y correjir error
			fecha = fecha.strftime('%m/%d/%Y')
			segundos = int(float(data[11:16]) - (5*60*60) )#GMZ -5

			H = int(segundos/(60*60))
			M = int((segundos/60)-(H*60))
			S = int(segundos - (H*60*60) - (M*60))

		
			hora = fecha+"   "+str(H)+":"+str(M)+":"+str(S)
			#hora = "NO YET"

			base = (lat, lon, hora)

			cursor.execute(insertar, base)

			# Make sure data is committed to the database
			mateo.commit()
		else:
			print("")

			#cursor.close()
			#mateo.close()

main()
