import csv,os, numpy, math
from itertools import islice
import datetime

title = ['PersonID', 'TripID', 'LinkID', 'Longitude','Latitude','Speed(kilometer)','DD/MM/YY','HH:MM:SS','GX','GY', 'Streetname', 'Streetlength', 'Speedlimit(mph)', 'Speedlimit(km/h)', 'speeding']

def addinfo():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = '/Users/toshiyokoo/Desktop/11_result'
	outputFile = open(os.path.join(root_path, filename[:-4] + '.csv'), 'a')
	writer = csv.writer(outputFile, lineterminator='\n')
	print >> outputFile, ','.join(title)
	for row in islice(reader, 1, None):
		list = []
		Filename = filename[:-4]
		personid = filename[0:6] + filename[7:9] + filename[10:12]
		longitude = str(row[0])
		latitude = str(row[1])
		speed = str(row[2])
		date = str(row[3])
		hms = str(row[4])
		GX = str(row[5])
		GY = str(row[6])
		streetname = str(row[8])
		streetlength = str(row[9])
		speedlimit = str(row[11])
		linkID = str(row[12])
		drive_speed = float(row[2])
			
		#convert the unit of speedlimit from mile to kilometer
		mile = float(row[11])
		conv_fac = 1.609344
		kilometer = mile * conv_fac
		
		#whether the speeding or not
		if (drive_speed - kilometer) > 0:
			speed2 = 1
		else:
			speed2 = 0
		
		list.extend([personid, Filename, linkID, longitude, latitude, speed, date, hms, GX, GY, streetname, streetlength, speedlimit, kilometer, speed2])
		writer.writerow(list)
	inputFile.close()
	print filename

path = "/Users/toshiyokoo/Desktop/aaaei"
for filename in os.listdir(path):
	global filename
	addinfo()
