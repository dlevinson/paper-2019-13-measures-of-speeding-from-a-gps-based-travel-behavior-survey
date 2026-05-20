# remove intersection & missing link GPS data

import csv,os, numpy, math
from itertools import islice
import time

#start = time.time()

global title1
title1 = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)','GX','GY']

def intersect():
	gps_inputFile1 = open(InDrPth1 +InFlnm1,'rU')
	gps_reader1 = csv.reader(gps_inputFile1)
	gps_inputFile1.seek(0)
	root_path1 = InDrPth2
	outputFile1 = open(os.path.join(root_path1,InFlnm1[:-4]+'.csv'),'a')
	writer1 = csv.writer(outputFile1, lineterminator='\n')
	print >> outputFile1, ','.join(title1)
	gis_inputFile1 = open(gis1,'rU')
	gis_reader1 = csv.reader(gis_inputFile1)
	min_height1 = 99 #dummy
	speedlimit1 = 99	#dummy
	for row1 in islice(gps_reader1, 1, None):
		list1 = []
		x_gps1 = float(row1[10])
		y_gps1 = float(row1[11])
		gis_inputFile1.seek(0)
		count1 = 0
		for j in islice(gis_reader1, 1, None):
			direction1 = float(j[42])
			ox_gis1 = float(j[43]) #OX
			oy_gis1 = float(j[44]) #OY
			dx_gis1 = float(j[45]) #DX
			dy_gis1 = float(j[46]) #DY
			if direction1 == 1:
				if (ox_gis1 - 10<= x_gps1 <= dx_gis1 + 10):
					if (oy_gis1 - 10) <= y_gps1 <= (dy_gis1 + 10):
						count1 += 1
					elif (dy_gis1 - 10) <= y_gps1 <= (oy_gis1 + 10):
						count1 += 1
				elif (dx_gis1 - 10 <= x_gps1 <= ox_gis1 + 10):
					if (oy_gis1 - 10) <= y_gps1 <= (dy_gis1 + 10):
						count1 += 1
					elif (dy_gis1 - 10) <= y_gps1 <= (oy_gis1 + 10):
						count1 += 1
						
		if count1 == 1:
			print >> outputFile1, ','.join(row1)

	gis_inputFile1.close()
	gps_inputFile1.close()
	print InFlnm1
	#elapsed_time = time.time() - start
	#print("elapsed_time:{0}".format(elapsed_time))
	
#global filename, InDrPth2, InFlnm1, InFlnm2, gi1, gi2, gis1, gis2
intersect()
