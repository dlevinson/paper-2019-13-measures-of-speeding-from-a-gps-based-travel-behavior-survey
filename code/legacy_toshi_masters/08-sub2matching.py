# find nearlestlink between GPS point and GIS map
# calculate minimum height
# link nearlest(Streetname and Speedlimit)

import csv,os, numpy, math
from itertools import islice
import time

#start = time.time()

global title2
title2 = ['Longitude','Latitude','Speed(kilometer)','DD/MM/YY','HH:MM:SS','GX','GY','Min_hight','Streetname', 'Streetlength', 'Roadtype','Speedlimit(mph)']

def nearlink():
	gps_inputFile = open(InDrPth2 +InFlnm2,'rU')
	gps_reader = csv.reader(gps_inputFile)
	gps_inputFile.seek(0)
	root_path = '/Users/toshiyokoo/Desktop/box'
	outputFile = open(os.path.join(root_path,InFlnm2[:-4]+'.csv'),'a')
	writer = csv.writer(outputFile, lineterminator='\n')
	print >> outputFile, ','.join(title2)
	gis_inputFile = open(gis2,'rU')
	gis_reader = csv.reader(gis_inputFile)
	min_height = 99 #dummy
	speedlimit = 99	#dummy
	for row in islice(gps_reader, 1, None):
		list = []
		x_gps = float(row[10])
		y_gps = float(row[11])
		longitude = str(row[0])
		latitude = str(row[1])
		speed = str(row[2])
		date = str(row[7])
		hms = str(row[8])
		GX = str(row[10])
		GY = str(row[11])
		gis_inputFile.seek(0)
		for i in islice(gis_reader, 1, None):
			direction = float(i[42])
			ox_gis = float(i[43]) #OX
			oy_gis = float(i[44]) #OY
			dx_gis = float(i[45]) #DX
			dy_gis = float(i[46]) #DY
			if direction == 1:
				if (ox_gis <= x_gps <= dx_gis):
					if (oy_gis - 30) <= y_gps <= (oy_gis + 30):
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
							#print '1', min_height
					elif (oy_gis <= y_gps <= dy_gis):	#road x-y & curve
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
					elif (dy_gis <= y_gps <= oy_gis):	#road x-y & curve
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
				elif (dx_gis <= x_gps <= ox_gis):
					if (oy_gis - 30) <= y_gps <= (oy_gis + 30):
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
							#print '1', min_height
					elif (oy_gis <= y_gps <= dy_gis):	#road x-y & curve
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
					elif (dy_gis <= y_gps <= oy_gis):	#road x-y & curve
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
				elif (oy_gis <= y_gps <= dy_gis):
					if (ox_gis - 30) <= x_gps <= (ox_gis + 30):	#road y-axis, interstate range 50m
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
				elif (dy_gis <= y_gps <= oy_gis):
					if (ox_gis - 30) <= x_gps <= (ox_gis + 30):	#road y-axis, interstate range 50m
						length = ((ox_gis - dx_gis) ** 2 + (oy_gis - dy_gis) ** 2) ** 0.5
						gis_o = numpy.array([ox_gis,oy_gis])
						gis_d = numpy.array([dx_gis,dy_gis])
						gps = numpy.array([x_gps,y_gps])
						v1 = gps - gis_o
						v2 = gis_d - gis_o
						Area = numpy.cross(v1, v2)
						D = abs(Area)
						height = D / length
						if 	min_height > height:
							min_height = height
							streetlength = str(i[0])
							streetname = str(i[5])
							roadtype = str(i[27])
							speedlimit = str(i[31])
			else:
				pass
						
		if min_height < 30:
			#streetlength = 99
			#streetname = 99	#dummy
			#roadtype = 99		#dummy
			#speedlimit = 99	#dummy
			Min_height = str(min_height)
			Streetname = str(streetname)
			Streetlength = str(streetlength)
			Roadtype = str(roadtype)
			Speedlimit = str(speedlimit)
			list.extend([longitude, latitude, speed, date, hms, GX, GY, Min_height, Streetname, Streetlength, Roadtype, Speedlimit])
			writer.writerow(list)
			#print >> outputFile, ','.join(row)
			min_height = 99 #dummy
			speedlimit = 99	#dummy
	gis_inputFile.close()
	gps_inputFile.close()

	print InFlnm2
	
	#elapsed_time = time.time() - start
	#print("elapsed_time:{0}".format(elapsed_time))

#global filename, InDrPth2, InFlnm2, gi1, gi2, gis1, gis2
nearlink()
