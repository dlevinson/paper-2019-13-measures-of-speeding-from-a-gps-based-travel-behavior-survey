# Remove data whose speed is less than 5km/h.
import csv,os
from itertools import islice

title = ['Longitude','Latitude','Speed(kilometer)','Course(degrees)','NumberOfSatellites','HDOP','Altitude(meters)','DD/MM/YY','HH:MM:SS','Distance(meters)']
def smallspeed():
	inputFile = open(path +'/' +filename,'rU')
	reader = csv.reader(inputFile)
	inputFile.seek(0)
	root_path = "/Users/toshiyokoo/Desktop/05_result"
	#dir_path = os.path.join(root_path,directory)
	#if not os.path.exists(dir_path):
	#	os.mkdir(dir_path)
	
	count = 0
	all_count = 0
	for row in islice(reader,1,None):
		if int(row[2]) > 5:
			count += 1
			all_count += 1
		else:
			all_count += 1
	
	inputFile.seek(0)
	if count == all_count:
		print filename[:-4] + 'is full'
		outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
		writer = csv.writer(outputFile)	
		print >> outputFile, ','.join(title)	
		for row in islice(reader,1,None):
			print >> outputFile, ','.join(row)
		outputFile.close()
	elif 0 < count < all_count:
		print filename[:-4] + 'is modified'
		outputFile = open(os.path.join(root_path,filename[:-4]+'.csv'),'a')
		writer = csv.writer(outputFile)	
		print >> outputFile, ','.join(title)
		for row in islice(reader,1,None):
			if int(row[2]) > 5:
				print >> outputFile, ','.join(row)
		outputFile.close()
	elif count == 0:
		print filename[:-4] + 'is empty'
	inputFile.close()

path = "/Users/toshiyokoo/Desktop/aaady"
for filename in os.listdir(path):
	global filename
	smallspeed()
