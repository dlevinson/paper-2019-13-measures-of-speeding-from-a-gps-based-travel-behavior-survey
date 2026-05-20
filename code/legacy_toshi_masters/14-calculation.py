#inputfile is from csv file after the algorithm 10_removeSL0km

import csv,os, numpy, math
from itertools import islice

title = ['filename', 'tripid', 'date', 'time', 'speed(kilometer)', 'streetlength', 'speedlimit(mph)', 'speedlimit(km)', 'speed_limit_compliance', 'speed2']
	
path = "/Users/toshiyokoo/Desktop/aaahu"
newname = 99
for filename in os.listdir(path):
	inputFile = open(path +'/' +filename,'rU')
	root_path = '/Users/toshiyokoo/Desktop/14_result'
	outputFile = open(os.path.join(root_path, filename[0:12] + '.csv'), 'a')
	writer = csv.writer(outputFile, lineterminator='\n')
	Filename = filename[:-4]
	trip = filename[0:6] + filename[7:9] + filename[10:12]
	tripid = int(trip)
	list = []
	if tripid == newname:
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			speed_km = str(row[2])
			date = str(row[3])
			time = str(row[4])
			street_length = str(row[9])
			speedlimit_mph = str(row[11])
			drive_speed = float(row[2])
			#convert the unit of speedlimit from mile to kilometer
			mile = float(row[11])
			conv_fac = 1.609344
			speedlimit_km = mile * conv_fac
		
			#calculate speed limit compliance
			speed_limit_compliance = drive_speed / speedlimit_km
			
			#whether the speeding or not
			if (drive_speed - speedlimit_km) > 0:
				speed2 = 1
			else:
				speed2 = 0
			
			list.extend([Filename, trip, date, time, speed_km, street_length, speedlimit_mph, speedlimit_km, speed_limit_compliance, speed2])
			writer.writerow(list)
			list = []
			
		newname = tripid
		inputFile.close()
		outputFile.close()
		print filename, "1"
		
	else:
		print >> outputFile, ','.join(title)
		reader = csv.reader(inputFile)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			speed_km = str(row[2])
			date = str(row[3])
			time = str(row[4])
			street_length = str(row[9])
			speedlimit_mph = str(row[11])
			drive_speed = float(row[2])
			#convert the unit of speedlimit from mile to kilometer
			mile = float(row[11])
			conv_fac = 1.609344
			speedlimit_km = mile * conv_fac
		
			#calculate speed limit compliance
			speed_limit_compliance = drive_speed / speedlimit_km
			
			#whether the speeding or not
			if (drive_speed - speedlimit_km) > 0:
				speed2 = 1
			else:
				speed2 = 0
			
			list.extend([Filename, trip, date, time, speed_km, street_length, speedlimit_mph, speedlimit_km, speed_limit_compliance, speed2])
			writer.writerow(list)
			list = []
			
		newname = tripid
		inputFile.close()
		outputFile.close()
		print filename, "2"
