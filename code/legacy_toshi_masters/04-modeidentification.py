# This program is mode classification. Five kinds of modes are found in the trips.
# Walk, off-network public transport mode, bus, bicycle and car.

import csv, dateutil, os, math
from scipy import stats
from itertools import islice
from dateutil import parser
	
def distanceBus():
	busStopFile = open("/Users/toshiyokoo/Desktop/5133/bus_stop.csv",'rU')
	busStop = csv.reader(busStopFile)
	inputFile.seek(0)
	GPSLonS = 0
	GPSLatS = 0
	startBusstop = 0
	for row in islice(reader,1,None):
		if int(row[2])>= 10: #speed is larger than 10km/h
			changeLonS = float(row[0])
			changeLatS = float(row[1])
			Longi_rad = changeLonS * math.pi / 180		#Longitude_radians
			Lati_rad = changeLatS * math.pi / 180		#Latitude_radians
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
			GPSLonS = float(E)
			GPSLatS = float(N)
			#print GPSLonS, GPSLatS
			break
		else:
			GPSLonS = 0
			GPSLatS = 0
			startBusstop = 0
			
	i = 1
	GPSLonE = 0
	GPSLatE = 0
	endBusstop = 0
	for row in reversed(list(reader)):
		if i < fileCount - 2:
			if int(row[2])> 10: #speed is greater than 10km/h
				changeLonE = float(row[0])
				changeLatE = float(row[1])
				Longi_rad = changeLonE * math.pi / 180		#Longitude_radians
				Lati_rad = changeLatE * math.pi / 180		#Latitude_radians
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
				GPSLonE = float(E)
				GPSLatE = float(N)
				#print GPSLonE, GPSLatE
				break
			else:
				GPSLonE = 0
				GPSLatE = 0
				endBusstop = 0
		else:
			GPSLonE = 0
			GPSLatE = 0
			endBusstop = 0
		i +=1
	
	if (GPSLonS != 0 and GPSLatS != 0 and GPSLonE != 0 and GPSLatE != 0 and GPSLonS != GPSLonE and GPSLatS != GPSLatE):
		for row in islice(busStop, 1, None):
			busLonS = float(row[0])
			busLatS = float(row[1])
			dS = ((GPSLonS - busLonS) ** 2 + (GPSLatS - busLatS) ** 2) ** 0.5
			#print 'busS=', dS
			if dS <=50: #distance less than 50 meters
				startBusstop = 1
				#print startBusstop
				break
			else:
				startBusstop = 0
		
		busStopFile.seek(0) 
		for row in islice(busStop, 1, None):
			busLonE = float(row[0])
			busLatE = float(row[1])
			dE = ((GPSLonE - busLonE) ** 2 + (GPSLatE - busLatE) ** 2) ** 0.5
			#print 'busE=', dE
			if dE <=50: #distance less than 50 meters
				endBusstop = 1
				break
			else:
				endBusstop = 0
	else:
		startBusstop = 0
		endBusstop = 0
		
	if (startBusstop == 1 and endBusstop == 1):
		distanceBus = 1
	else:
		distanceBus = 0
		
	return distanceBus

def distanceTrain():
	trainStopFile = open("/Users/toshiyokoo/Desktop/5133/train_station.csv",'rU')
	trainStop = csv.reader(trainStopFile)
	inputFile.seek(0)
	GPSLonS = 0
	GPSLatS = 0
	startTrainstop = 0
	for row in islice(reader,1,None):
		if int(row[2])>= 10: #speed is larger than 10km/h
			TchangeLonS = float(row[0])
			TchangeLatS = float(row[1])
			Longi_rad = TchangeLonS * math.pi / 180		#Longitude_radians
			Lati_rad = TchangeLatS * math.pi / 180		#Latitude_radians
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
			GPSLonS = float(E)
			GPSLatS = float(N)
			break
		else:
			GPSLonS = 0
			GPSLatS = 0
			startTrainstop = 0
		
	i = 1
	GPSLonE = 0
	GPSLatE = 0
	endTrainstop = 0
	for row in reversed(list(reader)):
		if i < fileCount - 2:
			if int(row[2])> 10: #speed is greater than 10km/h
				TchangeLonE = float(row[0])
				TchangeLatE = float(row[1])
				Longi_rad = TchangeLonE * math.pi / 180		#Longitude_radians
				Lati_rad = TchangeLatE * math.pi / 180		#Latitude_radians
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
				GPSLonE = float(E)
				GPSLatE = float(N)
				break
			else:
				GPSLonE = 0
				GPSLatE = 0
				endTrainstop = 0
		else:
			GPSLonE = 0
			GPSLatE = 0
			endTrainstop = 0
		i +=1
	
	if (GPSLonS != 0 and GPSLatS != 0 and GPSLonE != 0 and GPSLatE != 0 and GPSLonS != GPSLonE and GPSLatS != GPSLatE):
		for row in islice(trainStop, 1, None):
			trainLonS = float(row[0])
			trainLatS = float(row[1])
			dS = ((GPSLonS - trainLonS) ** 2 + (GPSLatS - trainLatS) ** 2) ** 0.5
			#print 'trainS=', dS
			if dS <=150: #distance less than 150 meters
				startTrainstop = 1
				break
			else:
				startTrainstop = 0
		
		trainStopFile.seek(0)
		for row in islice(trainStop, 1, None):
			trainLonE = float(row[0])
			trainLatE = float(row[1])
			dE = ((GPSLonE - trainLonE) ** 2 + (GPSLatE - trainLatE) ** 2) ** 0.5
			#print 'trainE=', dE
			if dE <=150: #distance less than 150 meters
				endTrainstop = 1
				break
			else:
				endTrainstop = 0
	else:
		startTrainstop = 0
		endTrainstop = 0
		
	if (startTrainstop == 1 and endTrainstop == 1):
		distanceTrain = 1
	else:
		distanceTrain = 0
		
	return distanceTrain

title = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)']
def checkMode():
	fileNumber = 1
	numberWalk = 0
	numberBike = 0
	numberTrain = 0
	numberBus = 0
	numberDrive = 0
	numberError = 0
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	fileCount = len(inputFile.readlines())
	global inputFile,reader,fileCount
	inputFile.seek(0)
	count = 0
	speed = []
	for row in islice(reader, 1, None):
		count += 1
		speed.append(int(row[2]))
		if (count == 1):
#			startSpeed = (int(row[2]))
			startTime = parser.parse(row[8])
		if (count == fileCount-1):
			endTime = parser.parse(row[8])
	Cspeed = (sum((speed)) / count)
	print filename[:-4], Cspeed, stats.scoreatpercentile(speed, 85)
	inputFile.seek(0)
	if (endTime - startTime).seconds >=60:
		if ((sum((speed)) / count) <= 6 and stats.scoreatpercentile(speed, 85) <= 10 and max(speed) <=20):
			root_walk = '/Users/toshiyokoo/Desktop/04_result_walk'
			outputFile_walk = open(os.path.join(root_walk, filename[:-4] + '.csv'), 'a')
			print >> outputFile_walk, ','.join(title)
			for row in islice(reader,1,None):
				print >> outputFile_walk, ','.join(row)
			outputFile_walk.close()
			numberWalk +=1
		elif (distanceTrain()==1 and (sum((speed)) / count) >= 10):
			root_train = '/Users/toshiyokoo/Desktop/04_result_train'
			outputFile_train = open(os.path.join(root_train, filename[:-4] + '.csv'), 'a')
			print >> outputFile_train, ','.join(title)
			inputFile.seek(0)
			for row in islice(reader,1,None):
				print >> outputFile_train, ','.join(row)
			outputFile_train.close()
			numberTrain +=1
		elif (distanceBus()==1 and (sum((speed)) / count) >= 10):
			root_bus = '/Users/toshiyokoo/Desktop/04_result_bus'
			outputFile_bus = open(os.path.join(root_bus, filename[:-4] + '.csv'), 'a')
			print >> outputFile_bus, ','.join(title)
			inputFile.seek(0)
			for row in islice(reader,1,None):
				print >> outputFile_bus, ','.join(row)
			outputFile_bus.close()
			numberBus +=1
		elif (stats.scoreatpercentile(speed, 85) > 10 and stats.scoreatpercentile(speed, 85) < 20 and max(speed)<=30):
			root_bike = '/Users/toshiyokoo/Desktop/04_result_bike'
			outputFile_bike = open(os.path.join(root_bike, filename[:-4] + '.csv'), 'a')
			print >> outputFile_bike, ','.join(title)
			inputFile.seek(0)
			for row in islice(reader,1,None):
				print >> outputFile_bike, ','.join(row)
			outputFile_bike.close()
			numberBike +=1
		elif ((sum((speed)) / count) >= 10):
			root_drive = '/Users/toshiyokoo/Desktop/04_result_drive'
			outputFile_drive = open(os.path.join(root_drive, filename[:-4] + '.csv'), 'a')
			print >> outputFile_drive, ','.join(title)
			inputFile.seek(0)
			for row in islice(reader,1,None):
				print >> outputFile_drive, ','.join(row)
			outputFile_drive.close()
			numberDrive +=1
		else:
			root_error = '/Users/toshiyokoo/Desktop/04_result_error'
			outputFile_error = open(os.path.join(root_error, filename[:-4] + '.csv'), 'a')
			print >> outputFile_error, ','.join(title)
			inputFile.seek(0)
			for row in islice(reader,1,None):
				print >> outputFile_error, ','.join(row)
			outputFile_error.close()
			numberError +=1
	else:
		root_error = '/Users/toshiyokoo/Desktop/04_result_error'
		outputFile_error = open(os.path.join(root_error, filename[:-4] + '.csv'), 'a')
		print >> outputFile_error, ','.join(title)
		inputFile.seek(0)
		for row in islice(reader,1,None):
			print >> outputFile_error, ','.join(row)
		outputFile_error.close()
		numberError +=1

path = "/Users/toshiyokoo/Desktop/aaadx"
for filename in os.listdir(path):
	global filename
	checkMode()
