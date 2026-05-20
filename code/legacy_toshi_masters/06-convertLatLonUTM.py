# convert latitude & longitude to UTM data

import csv,os
from itertools import islice
import math

title = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)','GX','GY']
def convert():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = "/Users/toshiyokoo/Desktop/06_result"
	#dir_path = os.path.join(root_path,directory)
	#if not os.path.exists( dir_path):
	#	os.mkdir( dir_path)
	outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
	writer = csv.writer(outputFile)
	print >> outputFile, ','.join(title)

	for row in islice(reader, 1, None):
		Longi_deg = float(row[0])				#Longitude_degree
		Lati_deg = float(row[1])				#Latitude_degree
		Longi_rad = Longi_deg * math.pi / 180		#Longitude_radians
		Lati_rad = Lati_deg * math.pi / 180		#Latitude_radians
		f = 1 / 298.257223563					#inverse flattening
		n = f / (2 - f)
		a = 6378137								#equatorial radius (meter)
		A = (a / (1 + n)) * (1 + (n ** 2) / 4 + (n ** 4) / 64)
		alpha1 = 0.5 * n - 0.666666667 * n ** 2 + 0.3125 * 1.0 * n ** 3 #1/2, 2/3, 5/16
		alpha2 = 0.270833333 * n ** 2 - 0.6 * n ** 3	#13/48, 3/5
		alpha3 = 0.254166667 * n ** 3	#61/240
		t = math.sinh(math.atanh(math.sin(Lati_rad)) - ((2 * n ** 0.5) / (1 + n)) * math.atanh(((2 * n ** 0.5) / (1 + n))* math.sin(Lati_rad)))
		Initial_deg = 15 * 6 - 183				#zone15
		Initial_rad = Initial_deg * math.pi / 180
		xi = math.atan(t / math.cos(Longi_rad - Initial_rad))
		eta = math.atanh(math.sin(Longi_rad - Initial_rad) / ((1 + t ** 2) ** 0.5))
		E0 = 500000								#initial (meter)
		k0 = 0.9996
		E = E0 + k0 * A * (eta + alpha1 * math.cos(2 * xi) * math.sinh(2 * eta) + alpha2 * math.cos(4 * xi) * math.sinh(4 * eta) + alpha3 * math.cos(6 * xi) * math.sinh(6 * eta)) 
		N = k0 * A * (xi + alpha1 * math.sin(2 * xi) * math.cosh(2 * eta) + alpha2 * math.sin(4 * xi) * math.cosh(4 * eta) + alpha3 * math.sin(6 * xi) * math.cosh(6 * eta)) 
		East = str(E)
		North = str(N)
		row.extend([East,North])
		print >> outputFile, ','.join(row)
	print filename[:-4]
	inputFile.close()

path = "/Users/toshiyokoo/Desktop/aaaea"
for filename in os.listdir(path):
	global filename
	convert()
